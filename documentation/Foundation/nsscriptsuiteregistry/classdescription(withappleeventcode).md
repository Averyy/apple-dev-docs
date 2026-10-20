# classDescription(withAppleEventCode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the class description associated with the given four-character Apple event code, `code`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func classDescription(withAppleEventCode appleEventCode: FourCharCode) -> NSScriptClassDescription?
```

```objc
- (NSScriptClassDescription *) classDescriptionWithAppleEventCode:(FourCharCode) appleEventCode;
```

#### Discussion

Overriding behavior is important here. Multiple classes can have the same code if the classes have an uninterrupted linear inheritance from one another. For example, if class B is a subclass of A and class C is a subclass of B, and all three classes have the same four-character Apple event code, then this method returns the class description for class C.

## See Also

### Getting and Registering Class Descriptions
- [func classDescriptions(inSuite: String) -> [String : NSScriptClassDescription]?](./classdescriptions%28insuite%29.md)
  Returns the class descriptions contained in the suite identified by `suiteName`.
- [func register(NSScriptClassDescription)](./register%28_%29-9aplw.md)
  Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/classdescription(withappleeventcode:))*