# suggestedPageSize

**Framework**: ContactProvider  
**Kind**: property  
**Required**: Yes

Retrieves the suggested number of items to include in a page.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var suggestedPageSize: Int { get }
```

#### Discussion

This value is a suggested upper limit for the number of contact items you can pass in the aggregate calls to [`didEnumerate(_:)`](contactitemcontentobserver/didenumerate(_:).md). Exceeding this limit may result in memory issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemcontentobserver/suggestedpagesize)*