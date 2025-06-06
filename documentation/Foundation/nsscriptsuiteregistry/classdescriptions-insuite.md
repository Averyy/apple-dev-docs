# classDescriptions(inSuite:)

**Framework**: Foundation  
**Kind**: method

Returns the class descriptions contained in the suite identified by `suiteName`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func classDescriptions(inSuite suiteName: String) -> [String : NSScriptClassDescription]?
```

#### Discussion

Each class description (instance of [`NSScriptClassDescription`](nsscriptclassdescription.md)) in the returned dictionary is identified by class name.

## See Also

- [func classDescription(withAppleEventCode: FourCharCode) -> NSScriptClassDescription?](nsscriptsuiteregistry/classdescription(withappleeventcode:).md)
  Returns the class description associated with the given four-character Apple event code, `code`.
- [func register(NSScriptClassDescription)](nsscriptsuiteregistry/register(_:)-9aplw.md)
  Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/classdescriptions(insuite:))*