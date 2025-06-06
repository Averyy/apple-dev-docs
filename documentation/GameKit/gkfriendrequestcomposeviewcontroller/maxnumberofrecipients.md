# maxNumberOfRecipients()

**Framework**: GameKit  
**Kind**: method

Returns the maximum number of recipients permitted in a single request.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func maxNumberOfRecipients() -> Int
```

#### Return Value

The maximum number of recipients.

#### Discussion

If you add more recipients than the value returned from this method, GameKit throws an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/maxnumberofrecipients())*