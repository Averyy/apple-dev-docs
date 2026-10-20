# suggestedBatchSize

**Framework**: ContactProvider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Retrieves the suggested number of changed contact items to include in a batch.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var suggestedBatchSize: Int { get }
```

#### Discussion

This value is a suggested upper limit for the number of contact items you can pass in the aggregate calls to [`didUpdate(_:)`](./didupdate%28_%29.md) and [`didDelete(_:)`](./diddelete%28_%29.md). Exceeding this limit may result in memory issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemchangeobserver/suggestedbatchsize)*