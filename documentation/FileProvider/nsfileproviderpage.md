# NSFileProviderPage

**Framework**: File Provider  
**Kind**: struct

A synchronization point that represents the next batch of items to be returned by an enumerator.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderPage
```

#### Discussion

Your file provider should populate the page with the information it needs to partition items into batches and to systematically return a batch of data at a time. For example, a simple page could contain the index of the next item to return. A request to enumerate items from that page would then return a batch of items starting at the specified index.

## Topics

### Page Constants
- [static let initialPageSortedByName: NSData](nsfileproviderpage/initialpagesortedbyname.md)
  The initial batch of items when sorted by name.
- [static let initialPageSortedByDate: NSData](nsfileproviderpage/initialpagesortedbydate.md)
  The initial batch of items when sorted by date.
### Initializers
- [init(Data)](nsfileproviderpage/init(_:).md)
  Creates a new page structure from the given raw value.
- [init(rawValue: Data)](nsfileproviderpage/init(rawvalue:).md)
  Creates a new page structure from the given raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Defining Your File Provider’s Content](defining-your-file-provider-s-content.md)
  Create enumerators to specify your file provider’s content.
- [protocol NSFileProviderEnumerationObserver](nsfileproviderenumerationobserver.md)
  An observer that receives batches of items during enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderpage)*