# ModelJudgeError

**Framework**: Evaluations  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
enum ModelJudgeError
```

## Topics

### Enumeration Cases
- [ModelJudgeError.invalidResponse(_:)](./modeljudgeerror/invalidresponse%28_%29.md)
  The evaluator can’t interpret the model judge’s response as a valid score.
- [case invalidScore(dimension: String, value: String)](./modeljudgeerror/invalidscore%28dimension,value%29.md)
  A scoring dimension returns a value the evaluator can’t parse as a number.
- [case jsonDecodingFailed(response: String, underlying: any Error)](./modeljudgeerror/jsondecodingfailed%28response,underlying%29.md)
  The evaluator fails to decode the JSON from the model judge’s response.
- [case missingDimension(String, response: String)](./modeljudgeerror/missingdimension%28_,response%29.md)
  The model judge’s response is missing a required scoring dimension. The first associated value is the name of the missing dimension.
- [ModelJudgeError.noScaleValues(dimension:)](./modeljudgeerror/noscalevalues%28dimension%29.md)
  The scoring dimension has no scale values defined.

## Relationships

### Conforms To
- [Error](../Swift/error.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeerror)*