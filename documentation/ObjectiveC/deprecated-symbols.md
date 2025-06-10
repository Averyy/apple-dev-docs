# Deprecated Symbols

**Framework**: Objective-C Runtime

Review symbols that are no longer supported and find the replacements to use instead.

## Topics

### Deprecated Class Methods
- [class func defaultPlaceholder(for: Any?, with: NSBindingName) -> Any?](nsobject-swift.class/defaultplaceholder(for:with:).md)
  Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
- [class func setDefaultPlaceholder(Any?, for: Any?, with: NSBindingName)](nsobject-swift.class/setdefaultplaceholder(_:for:with:).md)
  Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
### Deprecated Methods
- [func accessibilityAttributeNames() -> [NSAccessibility.Attribute]](nsobject-swift.class/accessibilityattributenames.md)
  Returns an array of attribute names supported by the receiver.
- [func accessibilityAttributeValue(NSAccessibility.Attribute) -> Any?](nsobject-swift.class/accessibilityattributevalue(_:).md)
  Returns the value of the specified attribute in the receiver.
- [func accessibilityAttributeValue(NSAccessibility.ParameterizedAttribute, forParameter: Any?) -> Any?](nsobject-swift.class/accessibilityattributevalue(_:forparameter:).md)
  Returns the value of the receiver’s parameterized attribute corresponding to the specified attribute name and parameter.
- [func accessibilityActionDescription(NSAccessibility.Action) -> String?](nsobject-swift.class/accessibilityactiondescription(_:).md)
  Returns a localized description of the specified action.
- [func accessibilityActionNames() -> [NSAccessibility.Action]](nsobject-swift.class/accessibilityactionnames.md)
  Returns an array of action names supported by the accessibility element.
- [func accessibilityArrayAttributeCount(NSAccessibility.Attribute) -> Int](nsobject-swift.class/accessibilityarrayattributecount(_:).md)
  Returns the count of the specified accessibility array attribute.
- [func accessibilityArrayAttributeValues(NSAccessibility.Attribute, index: Int, maxCount: Int) -> [Any]](nsobject-swift.class/accessibilityarrayattributevalues(_:index:maxcount:).md)
  Returns a subarray of values of an accessibility array attribute.
- [func accessibilityIndex(ofChild: Any) -> Int](nsobject-swift.class/accessibilityindex(ofchild:).md)
  Returns the index of the specified accessibility child in the parent.
- [func accessibilityIsAttributeSettable(NSAccessibility.Attribute) -> Bool](nsobject-swift.class/accessibilityisattributesettable(_:).md)
  Returns a Boolean value that indicates whether the value for the specified attribute in the receiver can be set.
- [func accessibilityIsIgnored() -> Bool](nsobject-swift.class/accessibilityisignored.md)
  Returns a Boolean value indicating whether the receiver should be ignored in the parent-child accessibility hierarchy.
- [func accessibilityParameterizedAttributeNames() -> [NSAccessibility.ParameterizedAttribute]](nsobject-swift.class/accessibilityparameterizedattributenames.md)
  Returns a list of parameterized attribute names supported by the receiver.
- [func accessibilityPerformAction(NSAccessibility.Action)](nsobject-swift.class/accessibilityperformaction(_:).md)
  Performs the action associated with the specified action.
- [func accessibilitySetOverrideValue(Any?, forAttribute: NSAccessibility.Attribute) -> Bool](nsobject-swift.class/accessibilitysetoverridevalue(_:forattribute:).md)
  Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value.
- [func accessibilitySetValue(Any?, forAttribute: NSAccessibility.Attribute)](nsobject-swift.class/accessibilitysetvalue(_:forattribute:).md)
  Sets the value of the specified attribute in the receiver to the specified value.
- [func finalize()](nsobject-swift.class/finalize.md)
  The garbage collector invokes this method on the receiver before disposing of the memory it uses.
- [func fontManager(Any, willIncludeFont: String) -> Bool](nsobject-swift.class/fontmanager(_:willincludefont:).md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](nsobject-swift.class/namesofpromisedfilesdropped(atdestination:).md)
  Returns the names of the files that the receiver promises to create at a specified location.
- [func textStorageDidProcessEditing(Notification)](nsobject-swift.class/textstoragedidprocessediting(_:).md)
- [func textStorageWillProcessEditing(Notification)](nsobject-swift.class/textstoragewillprocessediting(_:).md)
- [optional func workflowController(_ controller: AMWorkflowController, didError error: any Error)](../Automator/AMWorkflowControllerDelegate/workflowController(_:didError:).md)
  Notifies the delegate when the workflow encounters an error.
- [optional func workflowController(_ controller: AMWorkflowController, didRun action: AMAction)](../Automator/AMWorkflowControllerDelegate/workflowController(_:didRun:).md)
  Notifies the delegate when the specified action finishes running.
- [optional func workflowController(_ controller: AMWorkflowController, willRun action: AMAction)](../Automator/AMWorkflowControllerDelegate/workflowController(_:willRun:).md)
  Notifies the delegate when the specified action is about to run.
- [optional func workflowControllerDidRun(_ controller: AMWorkflowController)](../Automator/AMWorkflowControllerDelegate/workflowControllerDidRun(_:).md)
  Notifies the delegate when the workflow controller object finishes running.
- [optional func workflowControllerDidStop(_ controller: AMWorkflowController)](../Automator/AMWorkflowControllerDelegate/workflowControllerDidStop(_:).md)
  Tells the delegate that the workflow controller object has stopped.
- [optional func workflowControllerWillRun(_ controller: AMWorkflowController)](../Automator/AMWorkflowControllerDelegate/workflowControllerWillRun(_:).md)
  Notifies the delegate when the workflow controller object is about to run.
- [optional func workflowControllerWillStop(_ controller: AMWorkflowController)](../Automator/AMWorkflowControllerDelegate/workflowControllerWillStop(_:).md)
  Tells the delegate that the workflow controller object is about to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/deprecated-symbols)*