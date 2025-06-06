# commandDescription(withAppleEventClass:andAppleEventCode:)

**Framework**: Foundation  
**Kind**: method

Returns the command description identified by a suite’s four-character Apple event code of the class (`eventClass`) and the four-character Apple event code of the command (`commandCode`).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func commandDescription(withAppleEventClass appleEventClassCode: FourCharCode, andAppleEventCode appleEventIDCode: FourCharCode) -> NSScriptCommandDescription?
```

## See Also

- [func commandDescriptions(inSuite: String) -> [String : NSScriptCommandDescription]?](nsscriptsuiteregistry/commanddescriptions(insuite:).md)
  Returns the command descriptions contained in the suite identified by `suiteName`.
- [func register(NSScriptCommandDescription)](nsscriptsuiteregistry/register(_:)-5mq91.md)
  Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/commanddescription(withappleeventclass:andappleeventcode:))*