# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a result that requires the user to select from an array of choices.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func disambiguation(with callRecordsToDisambiguate: [INCallRecord]) -> Self
```

```objc
+ (instancetype) disambiguationWithCallRecordsToDisambiguate:(NSArray<INCallRecord *> *) callRecordsToDisambiguate;
```

## Return Value

A new [`INCallRecordResolutionResult`](../incallrecordresolutionresult.md) object.

## Discussion

Use this method to create a result when one `INCallRecord` matches the given information, and you can’t definitively pick one. Ask the user to select from the objects you specify.

## Parameters

- `callRecordsToDisambiguate`: An array of [`INCallRecord`](../incallrecord.md) objects for the user to choose from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordresolutionresult/disambiguation(with:))*