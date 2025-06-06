# enumerateContent(in:for:)

**Framework**: ContactProvider  
**Kind**: method  
**Required**: Yes

Enumerates all items, batched in pages.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func enumerateContent(in page: ContactItemPage, for observer: any ContactItemContentObserver) async
```

#### Discussion

The system calls `enumerateContent(in:for:)` for each page of items to enumerate. Your implementation calls [`didFinishEnumeratingPage(upTo:)`](contactitemcontentobserver/didfinishenumeratingpage(upto:).md) after enumerating each page, excluding the last page. After enumerating the last page, your implementation calls [`didFinishEnumeratingContent(upTo:)`](contactitemcontentobserver/didfinishenumeratingcontent(upto:).md).

Your implementation can enumerate items in any order, but the order must be deterministic and resumable. The system starts a new content enumeration with [`initialPage`](contactitempage/initialpage.md).

During content enumeration, every [`ContactItemPage`](contactitempage.md) except [`initialPage`](contactitempage/initialpage.md) must use the same [`generationMarker`](contactitempage/generationmarker.md), which represents the state of the content at a specific point in time. Changes made during the content enumeration can sync later with a change enumeration.

## Parameters

- `page`: The page to enumerate items from.
- `observer`: The system observer that receives the content items and   enumeration state.

## See Also

- [struct ContactItemPage](contactitempage.md)
  A fixed offset into enumerating all contact items.
- [protocol ContactItemContentObserver](contactitemcontentobserver.md)
  A protocol that defines a system observer that receives a resumable enumeration of all items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemenumerator/enumeratecontent(in:for:))*