# AgeRangeService.Response.sharing(range:)

**Framework**: Declared Age Range  
**Kind**: case

Contains the person’s shared age range information.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
case sharing(range: AgeRangeService.AgeRange)
```

#### Discussion

When you receive this response, the person successfully shared their age information. Use the associated `AgeRange` value to make appropriate content decisions for your app.

## Parameters

- `range`: The age range information provided by the person.

## See Also

- [AgeRangeService.Response.declinedSharing](agerangeservice/response/declinedsharing.md)
  Indicates the person declined to share their age range with your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/response/sharing(range:))*