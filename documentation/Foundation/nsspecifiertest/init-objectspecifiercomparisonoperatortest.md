# init(objectSpecifier:comparisonOperator:test:)

**Framework**: Foundation  
**Kind**: init

Returns a specifier test initialized to evaluate a test object against an object specified by an object specifier using a given comparison operation.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(objectSpecifier obj1: NSScriptObjectSpecifier?, comparisonOperator compOp: NSSpecifierTest.TestComparisonOperation, test obj2: Any?)
```

#### Return Value

A specifier test initialized to evaluate (`obj2`) against an object specified by `obj1` using the comparison operation `compOp`.

## Parameters

- `obj1`: An object specifier.
- `compOp`: The comparison operation.
- `obj2`: The object against which to evaluate the object specified by  .

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspecifiertest/init(objectspecifier:comparisonoperator:test:))*