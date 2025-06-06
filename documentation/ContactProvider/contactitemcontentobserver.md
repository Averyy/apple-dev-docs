# ContactItemContentObserver

**Framework**: ContactProvider  
**Kind**: protocol

A protocol that defines a system observer that receives a resumable enumeration of all items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
protocol ContactItemContentObserver
```

#### Overview

Your implementation of [`enumerateContent(in:for:)`](contactitemenumerator/enumeratecontent(in:for:).md) receives an observer that conforms to this type. As you enumerate over your contact items, you provide them to the observer with the [`didEnumerate(_:)`](contactitemcontentobserver/didenumerate(_:).md) method.

## Topics

### Providing contact items
- [func didEnumerate([ContactItem])](contactitemcontentobserver/didenumerate(_:).md)
  Provides an array of contact items to the observer.
- [enum ContactItem](contactitem.md)
  An item in the contact database.
### Ending enumeration
- [func didFinishEnumeratingContent(upTo: Data)](contactitemcontentobserver/didfinishenumeratingcontent(upto:).md)
  Finishes the content enumeration to the observer.
- [func didFinishEnumeratingPage(upTo: ContactItemPage)](contactitemcontentobserver/didfinishenumeratingpage(upto:).md)
  Marks a page of items as completed.
- [struct ContactItemPage](contactitempage.md)
  A fixed offset into enumerating all contact items.
- [func didFinishEnumeratingContentWithError(any Error)](contactitemcontentobserver/didfinishenumeratingcontentwitherror(_:).md)
  Finishes the content enumeration with an error, indicating failure, to the observer.
### Optimizing enumeration
- [var suggestedPageSize: Int](contactitemcontentobserver/suggestedpagesize.md)
  Retrieves the suggested number of items to include in a page.

## See Also

- [protocol ContactItemChangeObserver](contactitemchangeobserver.md)
  A protocol that defines a system observer that receives a resumable enumeration of changed contact items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemcontentobserver)*