# finalizeForWebScript()

**Framework**: Objective-C Runtime  
**Kind**: method

Performs cleanup when the scripting environment is reset.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func finalizeForWebScript()
```

#### Discussion

This method is invoked on objects exposed to the scripting environment just before the scripting environment is reset. After invocation, the receiving object will no longer be referenced by the scripting environment. Further references to `WebScriptObject` instances created by the exposed object will be invalid and may produce unpredictable results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/finalizeforwebscript())*