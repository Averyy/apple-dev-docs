# accessibilityWarningValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The warning value for the level indicator.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (strong, nullable) id accessibilityWarningValue;
```

#### Discussion

Use this property for elements such as the battery level indicator. This property sets a boundary value. If the element’s value exceeds the boundary value, the element has reached a warning stage.

## See Also

### Setting content and values
- [accessibilityContents](./accessibilitycontents.md)
  The contents of the current accessibility element.
- [accessibilityCriticalValue](./accessibilitycriticalvalue.md)
  The critical value for the level indicator.
- [accessibilityIdentifier](./accessibilityidentifier.md)
  The accessibility element’s identity.
- [accessibilityMaxValue](./accessibilitymaxvalue.md)
  The maximum value for the accessibility element.
- [accessibilityMinValue](./accessibilityminvalue.md)
  The minimum value for the accessibility element.
- [accessibilityOrientation](./accessibilityorientation.md)
  The orientation of the accessibility element.
- [accessibilityProtectedContent](./accessibilityprotectedcontent.md)
  A Boolean value that determines whether the accessibility element contains protected content.
- [accessibilitySelected](./accessibilityselected.md)
  A Boolean value that determines whether the accessibility element is currently in a selected state.
- [accessibilityURL](./accessibilityurl.md)
  The URL for the accessibility element.
- [accessibilityValueDescription](./accessibilityvaluedescription.md)
  A human-readable description of the accessibility element’s value.
- [enum NSAccessibilityOrientation](../nsaccessibilityorientation.md)
  Values that indicate the orientation of accessibility elements, such as scroll bars and split views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilitywarningvalue)*