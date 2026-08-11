# AgeRangeService.Error.network

**Framework**: Declared Age Range  
**Kind**: case

Indicates a network or server issue prevented completing the age range request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
case network
```

#### Discussion

You receive this error when the system can’t reach the server to fetch or update the age range or related parental controls information. Retry the request when network conditions improve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/error/network)*