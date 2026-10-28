# register(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func register(_ commandDescription: NSScriptCommandDescription)
```

```objc
- (void) registerCommandDescription:(NSScriptCommandDescription *) commandDescription;
```

## Discussion

Also registers with the single, shared instance of [`NSAppleEventManager`](../nsappleeventmanager.md) to handle incoming Apple events that should be handled by the command.

## See Also

### Related Documentation
- [func register(NSScriptClassDescription)](./register%28_%29-9aplw.md)
  Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.
- [func loadSuite(with: [AnyHashable : Any], from: Bundle)](./loadsuite%28with,from%29.md)
  Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.
### Getting and Registering Command Descriptions
- [func commandDescriptions(inSuite: String) -> [String : NSScriptCommandDescription]?](./commanddescriptions%28insuite%29.md)
  Returns the command descriptions contained in the suite identified by `suiteName`.
- [func commandDescription(withAppleEventClass: FourCharCode, andAppleEventCode: FourCharCode) -> NSScriptCommandDescription?](./commanddescription%28withappleeventclass,andappleeventcode%29.md)
  Returns the command description identified by a suite’s four-character Apple event code of the class (`eventClass`) and the four-character Apple event code of the command (`commandCode`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/register(_:)-5mq91)*