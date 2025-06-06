# didFinishEnumeratingPage(upTo:)

**Framework**: ContactProvider  
**Kind**: method  
**Required**: Yes

Marks a page of items as completed.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func didFinishEnumeratingPage(upTo nextPage: ContactItemPage)
```

#### Discussion

Call this method only if there are more items to enumerate after this page. An interrupted content enumeration can resume in the future, continuing from this page. Calling this method saves the current page of items to the system Contacts database.

## Parameters

- `nextPage`: The   where the next content enumeration can continue.

## See Also

- [func didFinishEnumeratingContent(upTo: Data)](contactitemcontentobserver/didfinishenumeratingcontent(upto:).md)
  Finishes the content enumeration to the observer.
- [struct ContactItemPage](contactitempage.md)
  A fixed offset into enumerating all contact items.
- [func didFinishEnumeratingContentWithError(any Error)](contactitemcontentobserver/didfinishenumeratingcontentwitherror(_:).md)
  Finishes the content enumeration with an error, indicating failure, to the observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemcontentobserver/didfinishenumeratingpage(upto:))*