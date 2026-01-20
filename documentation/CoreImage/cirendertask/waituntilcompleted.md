# waitUntilCompleted()

**Framework**: Core Image  
**Kind**: method

Waits until the [`CIRenderTask`](cirendertask.md) finishes and returns.

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

#### Discussion

Synchronously blocks execution until the [`CIRenderTask`](cirendertask.md) either completes or fails (with error).  Calling this method after [`startTask(toRender:to:)`](cicontext/starttask(torender:to:).md) or [`startTask(toRender:from:to:at:)`](cicontext/starttask(torender:from:to:at:).md) makes the render task behave synchronously, as if the CPU and GPU were operating as a single unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirendertask/waituntilcompleted())*