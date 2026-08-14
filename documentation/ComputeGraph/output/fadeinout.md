# output::fadeInOut

**Framework**: Compute Graph  
**Kind**: func

Applies a smooth fade-in and fade-out animation to the rendered output.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void output::fadeInOut()
```

#### Discussion

This function modulates the output alpha to create a fade-in effect over the first 0.5 seconds of the element’s lifetime and a fade-out effect over the last 0.5 seconds before the element expires. The two fades are multiplied together with the existing alpha, producing a smooth lifecycle transition.

> **Note**: This node is not general purpose and will be moved Visual: ![Graph](/images/com.apple.computegraph/output__fadeInOut.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/fadeinout)*