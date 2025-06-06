# init(suiteName:className:dictionary:)

**Framework**: Foundation  
**Kind**: init

Initializes and returns a newly allocated instance of `NSScriptClassDescription`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init?(suiteName: String, className: String, dictionary classDeclaration: [AnyHashable : Any]?)
```

#### Return Value

The initialized instance. Returns `nil` if the event code value for the class description itself is missing or is not an `NSString`. Also returns `nil` if the superclass name or any of the subdictionaries of descriptions are not of the right type.

#### Discussion

This method registers `self` with the application’s global instance of [`NSScriptSuiteRegistry`](nsscriptsuiteregistry.md).

## Parameters

- `suiteName`: The name of the suite (in the application’s scriptability information) that the class belongs to. For example,  .
- `className`: The name of the class that this instance describes.
- `classDeclaration`: A class declaration dictionary of the sort that is valid in script suite property list files. This dictionary provides information about the class such as its attributes and relationships.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [Key-Value Coding Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/init(suitename:classname:dictionary:))*