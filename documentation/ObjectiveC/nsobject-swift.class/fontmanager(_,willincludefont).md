# fontManager(_:willIncludeFont:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Requests permission from the Font panel delegate to display the given font name in the Font panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`NSFontCollection`](../../AppKit/nsfontcollection.md) for providing filtered font lists.

## Declaration

```swift
func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool
```

```objc
- (BOOL) fontManager:(id) sender willIncludeFont:(NSString *) fontName;
```

## Return Value

If the Font panel delegate returns [`YES`](../yes.md), `fontName` is listed; if the delegate returns [`NO`](../no.md), it isn’t.

## Discussion

In macOS versions 10.2 and earlier, this method is invoked repeatedly as necessary whenever the Font panel needs updating, such as when the Font panel is first loaded, and when the user selects a family name to see which typefaces in that family are available. Your implementation should execute fairly quickly to ensure the responsiveness of the Font panel.

> ❗ **Important**:  This delegate method is not called in macOS versions 10.3 and later.

## Parameters

- `sender`: The font manager making the request.
- `fontName`: The full PostScript name of the font to display, such as Helvetica-BoldOblique or Helvetica-Narrow-Bold.

## See Also

### Deprecated Methods
- [func accessibilityAttributeNames() -> [NSAccessibility.Attribute]](./accessibilityattributenames%28%29.md)
  Returns an array of attribute names supported by the receiver.
- [func accessibilityAttributeValue(NSAccessibility.Attribute) -> Any?](./accessibilityattributevalue%28_%29.md)
  Returns the value of the specified attribute in the receiver.
- [func accessibilityAttributeValue(NSAccessibility.ParameterizedAttribute, forParameter: Any?) -> Any?](./accessibilityattributevalue%28_,forparameter%29.md)
  Returns the value of the receiver’s parameterized attribute corresponding to the specified attribute name and parameter.
- [func accessibilityActionDescription(NSAccessibility.Action) -> String?](./accessibilityactiondescription%28_%29.md)
  Returns a localized description of the specified action.
- [func accessibilityActionNames() -> [NSAccessibility.Action]](./accessibilityactionnames%28%29.md)
  Returns an array of action names supported by the accessibility element.
- [func accessibilityArrayAttributeCount(NSAccessibility.Attribute) -> Int](./accessibilityarrayattributecount%28_%29.md)
  Returns the count of the specified accessibility array attribute.
- [func accessibilityArrayAttributeValues(NSAccessibility.Attribute, index: Int, maxCount: Int) -> [Any]](./accessibilityarrayattributevalues%28_,index,maxcount%29.md)
  Returns a subarray of values of an accessibility array attribute.
- [func accessibilityIndex(ofChild: Any) -> Int](./accessibilityindex%28ofchild%29.md)
  Returns the index of the specified accessibility child in the parent.
- [func accessibilityIsAttributeSettable(NSAccessibility.Attribute) -> Bool](./accessibilityisattributesettable%28_%29.md)
  Returns a Boolean value that indicates whether the value for the specified attribute in the receiver can be set.
- [func accessibilityIsIgnored() -> Bool](./accessibilityisignored%28%29.md)
  Returns a Boolean value indicating whether the receiver should be ignored in the parent-child accessibility hierarchy.
- [func accessibilityParameterizedAttributeNames() -> [NSAccessibility.ParameterizedAttribute]](./accessibilityparameterizedattributenames%28%29.md)
  Returns a list of parameterized attribute names supported by the receiver.
- [func accessibilityPerformAction(NSAccessibility.Action)](./accessibilityperformaction%28_%29.md)
  Performs the action associated with the specified action.
- [func accessibilitySetOverrideValue(Any?, forAttribute: NSAccessibility.Attribute) -> Bool](./accessibilitysetoverridevalue%28_,forattribute%29.md)
  Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value.
- [func accessibilitySetValue(Any?, forAttribute: NSAccessibility.Attribute)](./accessibilitysetvalue%28_,forattribute%29.md)
  Sets the value of the specified attribute in the receiver to the specified value.
- [func fileManager(FileManager, shouldProceedAfterError: [AnyHashable : Any]) -> Bool](./filemanager%28_,shouldproceedaftererror%29.md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/fontmanager(_:willincludefont:))*