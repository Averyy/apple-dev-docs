# addMoreTime(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command AddMoreTime

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
func addMoreTime(with params: MTRMicrowaveOvenControlClusterAddMoreTimeParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func addMoreTime(with params: MTRMicrowaveOvenControlClusterAddMoreTimeParams) async throws
```

```objc
- (void) addMoreTimeWithParams:(MTRMicrowaveOvenControlClusterAddMoreTimeParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command is used to add more time to the CookTime attribute of the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermicrowaveovencontrol/addmoretime(with:completion:))*