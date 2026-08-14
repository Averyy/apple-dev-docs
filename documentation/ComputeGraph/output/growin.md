# output::growIn

**Framework**: Compute Graph  
**Kind**: func

Applies a smooth grow-in animation to the rendered output.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void output::growIn()
```

#### Discussion

This function scales the output size from 25% to 100% over the first 0.5 seconds of the element’s lifetime using a smooth interpolation. This creates a natural appearance effect where particles start small and grow to full size.

> **Note**: This node is not general purpose and will be moved Visual: ![Graph](/images/com.apple.computegraph/output__growIn.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/growin)*