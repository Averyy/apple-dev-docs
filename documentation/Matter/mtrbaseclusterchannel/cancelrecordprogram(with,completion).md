# cancelRecordProgram(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command CancelRecordProgram

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func cancelRecordProgram(with params: MTRChannelClusterCancelRecordProgramParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func cancelRecordProgram(with params: MTRChannelClusterCancelRecordProgramParams) async throws
```

```objc
- (void) cancelRecordProgramWithParams:(MTRChannelClusterCancelRecordProgramParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

Cancel recording for a specific program or series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterchannel/cancelrecordprogram(with:completion:))*