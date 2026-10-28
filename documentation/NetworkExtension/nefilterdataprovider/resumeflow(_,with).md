# resumeFlow(_:with:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Resumes a previously-paused flow.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func resumeFlow(_ flow: NEFilterFlow, with verdict: NEFilterVerdict)
```

```objc
- (void) resumeFlow:(NEFilterFlow *) flow withVerdict:(NEFilterVerdict *) verdict;
```

## Discussion

The provider calls this method to resume a flow that the provider previously paused by returning a pause verdict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/resumeflow(_:with:))*