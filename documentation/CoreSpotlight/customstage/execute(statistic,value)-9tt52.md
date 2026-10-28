# execute(statistic:value:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Generates output data from the specified statistical value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
nonisolated(nonsending)
func execute(statistic: String, value: Double) async throws -> SearchPipelineData
```

## Return Value

A pipeline data structure with data your stage produced. Make sure the output you return matches the output you specified in the [`outputType`](./outputtype.md) property.

## Discussion

If your stage supports a statistical value as input, implement this method and use it to generate your stage’s supported output data. Write your code to run in parallel with other instances of your stage and instances of other stages. The best approach is to use only the contents of the `items` parameter and local intermediate values you create to deliver the output data.

## Parameters

- `statisticName`: The name of the statistic. This parameter contains strings like “average”, “max”, “min”, “sum”, “median”, or “stddev”.
- `value`: The value for the statistic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/execute(statistic:value:)-9tt52)*