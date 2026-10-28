# waitUntilCompleted()

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Waits until the [`CIRenderTask`](../cirendertask.md) finishes and returns.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func waitUntilCompleted() throws -> CIRenderInfo
```

```objc
- (CIRenderInfo *) waitUntilCompletedAndReturnError:(NSError **) error;
```

## Discussion

Synchronously blocks execution until the [`CIRenderTask`](../cirendertask.md) either completes or fails (with error).  Calling this method after [`startTask(toRender:to:)`](../cicontext/starttask%28torender,to%29.md) or [`startTask(toRender:from:to:at:)`](../cicontext/starttask%28torender,from,to,at%29.md) makes the render task behave synchronously, as if the CPU and GPU were operating as a single unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirendertask/waituntilcompleted())*