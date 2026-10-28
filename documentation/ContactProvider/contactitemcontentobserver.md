# ContactItemContentObserver

**Framework**: ContactProvider  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines a system observer that receives a resumable enumeration of all items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
protocol ContactItemContentObserver
```

## Overview

Your implementation of [`enumerateContent(in:for:)`](./contactitemenumerator/enumeratecontent%28in,for%29.md) receives an observer that conforms to this type. As you enumerate over your contact items, you provide them to the observer with the [`didEnumerate(_:)`](./contactitemcontentobserver/didenumerate%28_%29.md) method.

## Topics

### Providing contact items
- [func didEnumerate([ContactItem])](./contactitemcontentobserver/didenumerate%28_%29.md)
  Provides an array of contact items to the observer.
- [enum ContactItem](./contactitem.md)
  An item in the contact database.
### Ending enumeration
- [func didFinishEnumeratingContent(upTo: Data)](./contactitemcontentobserver/didfinishenumeratingcontent%28upto%29.md)
  Finishes the content enumeration to the observer.
- [func didFinishEnumeratingPage(upTo: ContactItemPage)](./contactitemcontentobserver/didfinishenumeratingpage%28upto%29.md)
  Marks a page of items as completed.
- [struct ContactItemPage](./contactitempage.md)
  A fixed offset into enumerating all contact items.
- [func didFinishEnumeratingContentWithError(any Error)](./contactitemcontentobserver/didfinishenumeratingcontentwitherror%28_%29.md)
  Finishes the content enumeration with an error, indicating failure, to the observer.
### Optimizing enumeration
- [var suggestedPageSize: Int](./contactitemcontentobserver/suggestedpagesize.md)
  Retrieves the suggested number of items to include in a page.

## See Also

### Receiving contacts
- [protocol ContactItemChangeObserver](./contactitemchangeobserver.md)
  A protocol that defines a system observer that receives a resumable enumeration of changed contact items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemcontentobserver)*