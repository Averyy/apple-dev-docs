# ModelJudgeError

**Framework**: Evaluations  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
enum ModelJudgeError
```

## Topics

### Enumeration Cases
- [ModelJudgeError.invalidResponse(_:)](modeljudgeerror/invalidresponse(_:).md)
  The evaluator can’t interpret the model judge’s response as a valid score.
- [case invalidScore(dimension: String, value: String)](modeljudgeerror/invalidscore(dimension:value:).md)
  A scoring dimension returns a value the evaluator can’t parse as a number.
- [case jsonDecodingFailed(response: String, underlying: any Error)](modeljudgeerror/jsondecodingfailed(response:underlying:).md)
  The evaluator fails to decode the JSON from the model judge’s response.
- [case missingDimension(String, response: String)](modeljudgeerror/missingdimension(_:response:).md)
  The model judge’s response is missing a required scoring dimension. The first associated value is the name of the missing dimension.
- [ModelJudgeError.noScaleValues(dimension:)](modeljudgeerror/noscalevalues(dimension:).md)
  The scoring dimension has no scale values defined.

## Relationships

### Conforms To
- [Error](../swift/error.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modeljudgeerror)*