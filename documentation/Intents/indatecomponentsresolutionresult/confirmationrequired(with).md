# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func confirmationRequired(with dateComponentsToConfirm: DateComponents?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithDateComponentsToConfirm:(NSDateComponents *) dateComponentsToConfirm;
```

#### Return Value

A new [`INDateComponentsResolutionResult`](../indatecomponentsresolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter to a single object but you want the user to confirm that value before proceeding. You might ask for confirmation when there is some doubt that the specified object is what the user intended. For example, when booking a restaurant reservation, you might ask the user to confirm a date that is close, but not exactly the same, to the one that was requested.

## Parameters

- `dateComponentsToConfirm`: The date for the user to confirm.

## See Also

### Creating a Resolution Result Object
- [class func success(with: DateComponents) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [DateComponents]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsresolutionresult/confirmationrequired(with:))*