# register(_:)

**Framework**: Foundation  
**Kind**: method

Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func register(_ classDescription: NSScriptClassDescription)
```

## See Also

- [func loadSuite(with: [AnyHashable : Any], from: Bundle)](nsscriptsuiteregistry/loadsuite(with:from:).md)
  Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.
- [func register(NSScriptCommandDescription)](nsscriptsuiteregistry/register(_:)-5mq91.md)
  Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.
- [func classDescriptions(inSuite: String) -> [String : NSScriptClassDescription]?](nsscriptsuiteregistry/classdescriptions(insuite:).md)
  Returns the class descriptions contained in the suite identified by `suiteName`.
- [func classDescription(withAppleEventCode: FourCharCode) -> NSScriptClassDescription?](nsscriptsuiteregistry/classdescription(withappleeventcode:).md)
  Returns the class description associated with the given four-character Apple event code, `code`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/register(_:)-9aplw)*