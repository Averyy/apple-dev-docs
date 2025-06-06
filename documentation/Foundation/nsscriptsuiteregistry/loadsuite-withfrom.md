# loadSuite(with:from:)

**Framework**: Foundation  
**Kind**: method

Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func loadSuite(with suiteDeclaration: [AnyHashable : Any], from bundle: Bundle)
```

#### Discussion

The method extracts information from the dictionary and caches it in various internal collection objects. If keys are missing or values are of the wrong type, it logs messages to the console. It also registers class descriptions and command descriptions. In registering a class description, it invokes the [`NSClassDescription`](nsclassdescription.md) class method [`register(_:for:)`](nsclassdescription/register(_:for:).md). In registering a command description, it arranges for the Apple event translator to handle incoming Apple events that represent the defined commands.

This method is invoked when the shared instance is initialized and when bundles are loaded at runtime. Prior to invoking it, `NSScriptSuiteRegistry` creates the dictionary argument from the `.scriptSuite` property list. If you invoke this method in your code, you should try to do it before the application receives its first Apple event.

## See Also

- [func register(NSScriptClassDescription)](nsscriptsuiteregistry/register(_:)-9aplw.md)
  Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.
- [class func shared() -> NSScriptSuiteRegistry](nsscriptsuiteregistry/shared.md)
  Returns the single, shared instance of `NSScriptSuiteRegistry`, creating it first if it doesn’t exist.
- [func register(NSScriptCommandDescription)](nsscriptsuiteregistry/register(_:)-5mq91.md)
  Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.
- [func loadSuites(from: Bundle)](nsscriptsuiteregistry/loadsuites(from:).md)
  Loads the suite definitions in bundle `aBundle`, invoking [`loadSuite(with:from:)`](nsscriptsuiteregistry/loadsuite(with:from:).md) for each suite found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/loadsuite(with:from:))*