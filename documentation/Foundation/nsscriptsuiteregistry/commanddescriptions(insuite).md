# commandDescriptions(inSuite:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the command descriptions contained in the suite identified by `suiteName`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func commandDescriptions(inSuite suiteName: String) -> [String : NSScriptCommandDescription]?
```

```objc
- (NSDictionary<NSString *,NSScriptCommandDescription *> *) commandDescriptionsInSuite:(NSString *) suiteName;
```

## Discussion

Each command description (instance of [`NSScriptCommandDescription`](../nsscriptcommanddescription.md)) in the returned dictionary is identified by command name.

## See Also

### Getting and Registering Command Descriptions
- [func commandDescription(withAppleEventClass: FourCharCode, andAppleEventCode: FourCharCode) -> NSScriptCommandDescription?](./commanddescription%28withappleeventclass,andappleeventcode%29.md)
  Returns the command description identified by a suite’s four-character Apple event code of the class (`eventClass`) and the four-character Apple event code of the command (`commandCode`).
- [func register(NSScriptCommandDescription)](./register%28_%29-5mq91.md)
  Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/commanddescriptions(insuite:))*