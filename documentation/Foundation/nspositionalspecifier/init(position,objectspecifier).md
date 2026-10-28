# init(position:objectSpecifier:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a positional specifier with a given position relative to another given specifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(position: NSPositionalSpecifier.InsertionPosition, objectSpecifier specifier: NSScriptObjectSpecifier)
```

```objc
- (instancetype) initWithPosition:(NSInsertionPosition) position objectSpecifier:(NSScriptObjectSpecifier *) specifier;
```

## Return Value

An initialized positional specifier with the position specified by `position` relative to the object specified by `specifier`.

## Parameters

- `position`: The position for the new specifier relative to `specifier`.
- `specifier`: The reference specifier.

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspositionalspecifier/init(position:objectspecifier:))*