# didEnumerate(_:)

**Framework**: ContactProvider  
**Kind**: method  
**Required**: Yes

Provides an array of contact items to the observer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func didEnumerate(_: [ContactItem])
```

#### Discussion

You can call this method multiple times to fulfill the [`suggestedPageSize`](contactitemcontentobserver/suggestedpagesize.md).

## See Also

- [enum ContactItem](contactitem.md)
  An item in the contact database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemcontentobserver/didenumerate(_:))*