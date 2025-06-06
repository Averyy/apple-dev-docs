# ContactItemEnumerator

**Framework**: ContactProvider  
**Kind**: protocol

A protocol to provide enumerations of all contact items and changed contact items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
protocol ContactItemEnumerator
```

#### Overview

Implement this protocol to fetch contact items from your data store in a consistent, predictable order when the system requests contact item enumeration. The [`ContactItemEnumerating`](contactitemenumerating.md) protocol, typically implemented by the app extension, returns an instance of this type when the system requests contacts.

The enumerator has two main methods to implement:

- [`enumerateContent(in:for:)`](contactitemenumerator/enumeratecontent(in:for:).md) – Enumerates all of your contacts that you want to provide to the system-wide Contacts ecosystem, sending arrays of [`ContactItem`](contactitem.md) instances to a [`ContactItemContentObserver`](contactitemcontentobserver.md).
- [`enumerateChanges(startingAt:for:)`](contactitemenumerator/enumeratechanges(startingat:for:).md) – Enumerates changed contacts, sending updates and deletions to a [`ContactItemChangeObserver`](contactitemchangeobserver.md), as arrays of [`ContactItem`](contactitem.md) and [`ContactItem.Identifier`](contactitem/identifier.md) instances, respectively.

The following `RootContainerEnumerator` outlines how to implement a `ContactItemEnumerator`. The listing shows `TODO` in places where the implementation depends on the specifics of your app’s data store.

```swift
import ContactProvider

class RootContainerEnumerator: ContactItemEnumerator {

    func configure(for domain: ContactProviderDomain) {
        // Configure your enumerator here.
    }
    
    func enumerateContent(in page: ContactItemPage, 
                          for observer: any ContactItemContentObserver) {

        // TODO: Get the database generation for the content enumeration, which is used for the first call to `enumerateChanges`.
        let generationMarker = (page == .initialPage) ? currentGenerationMarker() : page.generationMarker

        do {
            // TODO: Get your batch of items to enumerate.
            let content = try fetchContent(startingAt: generationMarker,
                                           offset: page.offset,
                                           count: observer.suggestedPageSize)
            
            // Send the items to the observer.
            observer.didEnumerate(content.items)

            if content.moreComing {
                // Need to enumerate more items.
            
                // TODO: Create your next `ItemPage` that starts the next batch of items.
                //
                // Note: If `page.generationMarker` is empty, you must provide a non-empty `nextPage.generationMarker`.
                //       If `page.generationMarker` is non-empty, `nextPage.generationMarker` must be the same value.
                let nextPage = ContactItemPage(generationMarker: generationMarker,
                                               offset: page.offset + content.items.count)

                // Send the observer to the next page.
                observer.didFinishEnumeratingPage(upTo: nextPage)
            } else {
                // All items have been enumerated.
                
                // Tell the observer the next sync should be a change enumeration.
                observer.didFinishEnumeratingContent(upTo: generationMarker)
            }

        } catch {
            // Tell the observer an error occurred.
            //
            // Note: The system resumes the enumeration from the last `ContactItemPage` that was enumerated successfully, if the error is resumable.
            observer.didFinishEnumeratingContentWithError(error)
        }
        
        func currentGenerationMarker() -> Data {
            // TODO: Get the value specific to your data source identifying the current database generation.
            //
            // Note: Don't call `didFinishEnumeratingPage(upTo:)` with an empty `ContactItemPage.generationMarker`; this results in an error.
            let generationMarker: Data = "<currentDatabaseGenerationMarker>".data(using: .utf8)!
            return generationMarker
        }

        func fetchContent(startingAt generationMarker: Data, offset: Int, count: Int) throws -> ContentFetchResult {
            // TODO: Fetch up to `count` items from the database, starting at `offset` items for the database generation specified by `generationMarker`.
            let items: [ContactItem] = []
            let moreComing: Bool = false

            return ContentFetchResult(items: items, moreComing: moreComing)
        }

        struct ContentFetchResult {
            let items: [ContactItem]
            let moreComing: Bool
        }

    }
    
    func enumerateChanges(startingAt syncAnchor: ContactItemSyncAnchor, 
                          for observer: any ContactItemChangeObserver) {
        do {
            // TODO: Get your batch of changed items to enumerate.
            let changes = try fetchChanges(startingAt: syncAnchor.generationMarker,
                                           offset: syncAnchor.offset,
                                           count: observer.suggestedBatchSize)

            // Send the changes to the observer.
            observer.didUpdate(changes.updatedItems)
            observer.didDelete(changes.deletedItemIdentifiers)
            observer.didFinishEnumeratingChanges(upTo: changes.nextSyncAnchor,
                                                 moreComing: changes.moreComing)
        } catch {
            // Tell the observer an error occurred.
            //
            // Note: The system resumes the enumeration from the last `ItemChangeAnchor` that was enumerated successfully, if the error is resumable.
            observer.didFinishEnumeratingChangesWithError(error)
        }

        func fetchChanges(startingAt generationMarker: Data, offset: Int, count: Int) throws -> ChangeFetchResult {
            // TODO: Fetch up to `count` changes from the database, starting at `offset` changes after the database generation specified by `generationMarker`.
            let updatedItems: [ContactItem] = []
            let deletedItemIdentifiers: [ContactItem.Identifier] = []
            let moreComing: Bool = false

            // TODO: Generate the next `ContactItemSyncAnchor`, using the `generationMarker` and offset of the last change that was fetched.
            let lastChangeGenerationMarker: Data = "<lastChangeGenerationMarker>".data(using: .utf8)!
            let lastChangeOffset: Int = 0
            let nextSyncAnchor = ContactItemSyncAnchor(generationMarker: lastChangeGenerationMarker, offset: lastChangeOffset)

            return ChangeFetchResult(updatedItems: updatedItems,
                                     deletedItemIdentifiers: deletedItemIdentifiers,
                                     moreComing: moreComing,
                                     nextSyncAnchor: nextSyncAnchor)
        }

        struct ChangeFetchResult {
            let updatedItems: [ContactItem]
            let deletedItemIdentifiers: [ContactItem.Identifier]
            let moreComing: Bool
            let nextSyncAnchor: ContactItemSyncAnchor
        }
    }
    
    func invalidate() async {
        // Invalidate here.
    }
}
```

## Topics

### Enumerating contact items
- [func enumerateContent(in: ContactItemPage, for: any ContactItemContentObserver) async](contactitemenumerator/enumeratecontent(in:for:).md)
  Enumerates all items, batched in pages.
- [struct ContactItemPage](contactitempage.md)
  A fixed offset into enumerating all contact items.
- [protocol ContactItemContentObserver](contactitemcontentobserver.md)
  A protocol that defines a system observer that receives a resumable enumeration of all items.
### Enumerating item changes
- [func enumerateChanges(startingAt: ContactItemSyncAnchor, for: any ContactItemChangeObserver) async](contactitemenumerator/enumeratechanges(startingat:for:).md)
  Enumerates items changed since the last sync.
- [struct ContactItemSyncAnchor](contactitemsyncanchor.md)
  A snapshot point into enumerating changed contact items.
- [protocol ContactItemChangeObserver](contactitemchangeobserver.md)
  A protocol that defines a system observer that receives a resumable enumeration of changed contact items.
### Managing enumerator life cycle
- [func invalidate() async](contactitemenumerator/invalidate.md)
  Invalidates the enumerator.

## See Also

- [enum ContactItem](contactitem.md)
  An item in the contact database.
- [protocol ContactItemEnumerating](contactitemenumerating.md)
  A protocol to provide enumerators for collections of contact items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemenumerator)*