# register(_:)

**Framework**: Foundation  
**Kind**: method

Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func register(_ commandDescription: NSScriptCommandDescription)
```

#### Discussion

Also registers with the single, shared instance of [`NSAppleEventManager`](nsappleeventmanager.md) to handle incoming Apple events that should be handled by the command.

## See Also

- [func register(NSScriptClassDescription)](nsscriptsuiteregistry/register(_:)-9aplw.md)
  Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.
- [func loadSuite(with: [AnyHashable : Any], from: Bundle)](nsscriptsuiteregistry/loadsuite(with:from:).md)
  Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.
- [func commandDescriptions(inSuite: String) -> [String : NSScriptCommandDescription]?](nsscriptsuiteregistry/commanddescriptions(insuite:).md)
  Returns the command descriptions contained in the suite identified by `suiteName`.
- [func commandDescription(withAppleEventClass: FourCharCode, andAppleEventCode: FourCharCode) -> NSScriptCommandDescription?](nsscriptsuiteregistry/commanddescription(withappleeventclass:andappleeventcode:).md)
  Returns the command description identified by a suite’s four-character Apple event code of the class (`eventClass`) and the four-character Apple event code of the command (`commandCode`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/register(_:)-5mq91)*