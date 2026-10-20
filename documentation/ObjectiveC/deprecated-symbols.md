# Deprecated Symbols

**Framework**: Objective-C Runtime  
**Role**: API Collection

Review symbols that are no longer supported and find the replacements to use instead.

## Topics

### Deprecated Class Methods
- [class func defaultPlaceholder(for: Any?, with: NSBindingName) -> Any?](./nsobject-swift.class/defaultplaceholder%28for,with%29.md)
  Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
- [class func setDefaultPlaceholder(Any?, for: Any?, with: NSBindingName)](./nsobject-swift.class/setdefaultplaceholder%28_,for,with%29.md)
  Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
- [class func useStoredAccessor() -> Bool](./nsobject-swift.class/usestoredaccessor%28%29.md)
  Returns `true` if the stored value methods [`storedValue(forKey:)`](./nsobject-swift.class/storedvalue%28forkey%29.md) and [`takeStoredValue(_:forKey:)`](./nsobject-swift.class/takestoredvalue%28_,forkey%29.md) should use private accessor methods in preference to public accessors.
### Deprecated Methods
- [func accessibilityAttributeNames() -> [NSAccessibility.Attribute]](./nsobject-swift.class/accessibilityattributenames%28%29.md)
  Returns an array of attribute names supported by the receiver.
- [func accessibilityAttributeValue(NSAccessibility.Attribute) -> Any?](./nsobject-swift.class/accessibilityattributevalue%28_%29.md)
  Returns the value of the specified attribute in the receiver.
- [func accessibilityAttributeValue(NSAccessibility.ParameterizedAttribute, forParameter: Any?) -> Any?](./nsobject-swift.class/accessibilityattributevalue%28_,forparameter%29.md)
  Returns the value of the receiver’s parameterized attribute corresponding to the specified attribute name and parameter.
- [func accessibilityActionDescription(NSAccessibility.Action) -> String?](./nsobject-swift.class/accessibilityactiondescription%28_%29.md)
  Returns a localized description of the specified action.
- [func accessibilityActionNames() -> [NSAccessibility.Action]](./nsobject-swift.class/accessibilityactionnames%28%29.md)
  Returns an array of action names supported by the accessibility element.
- [func accessibilityArrayAttributeCount(NSAccessibility.Attribute) -> Int](./nsobject-swift.class/accessibilityarrayattributecount%28_%29.md)
  Returns the count of the specified accessibility array attribute.
- [func accessibilityArrayAttributeValues(NSAccessibility.Attribute, index: Int, maxCount: Int) -> [Any]](./nsobject-swift.class/accessibilityarrayattributevalues%28_,index,maxcount%29.md)
  Returns a subarray of values of an accessibility array attribute.
- [func accessibilityIndex(ofChild: Any) -> Int](./nsobject-swift.class/accessibilityindex%28ofchild%29.md)
  Returns the index of the specified accessibility child in the parent.
- [func accessibilityIsAttributeSettable(NSAccessibility.Attribute) -> Bool](./nsobject-swift.class/accessibilityisattributesettable%28_%29.md)
  Returns a Boolean value that indicates whether the value for the specified attribute in the receiver can be set.
- [func accessibilityIsIgnored() -> Bool](./nsobject-swift.class/accessibilityisignored%28%29.md)
  Returns a Boolean value indicating whether the receiver should be ignored in the parent-child accessibility hierarchy.
- [func accessibilityParameterizedAttributeNames() -> [NSAccessibility.ParameterizedAttribute]](./nsobject-swift.class/accessibilityparameterizedattributenames%28%29.md)
  Returns a list of parameterized attribute names supported by the receiver.
- [func accessibilityPerformAction(NSAccessibility.Action)](./nsobject-swift.class/accessibilityperformaction%28_%29.md)
  Performs the action associated with the specified action.
- [func accessibilitySetOverrideValue(Any?, forAttribute: NSAccessibility.Attribute) -> Bool](./nsobject-swift.class/accessibilitysetoverridevalue%28_,forattribute%29.md)
  Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value.
- [func accessibilitySetValue(Any?, forAttribute: NSAccessibility.Attribute)](./nsobject-swift.class/accessibilitysetvalue%28_,forattribute%29.md)
  Sets the value of the specified attribute in the receiver to the specified value.
- [func fileManager(FileManager, shouldProceedAfterError: [AnyHashable : Any]) -> Bool](./nsobject-swift.class/filemanager%28_,shouldproceedaftererror%29.md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(FileManager, willProcessPath: String)](./nsobject-swift.class/filemanager%28_,willprocesspath%29.md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.
- [func finalize()](./nsobject-swift.class/finalize%28%29.md)
  The garbage collector invokes this method on the receiver before disposing of the memory it uses.
- [func fontManager(Any, willIncludeFont: String) -> Bool](./nsobject-swift.class/fontmanager%28_,willincludefont%29.md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](./nsobject-swift.class/namesofpromisedfilesdropped%28atdestination%29.md)
  Returns the names of the files that the receiver promises to create at a specified location.
- [func storedValue(forKey: String) -> Any?](./nsobject-swift.class/storedvalue%28forkey%29.md)
  Returns the property identified by a given key.
- [func textStorageDidProcessEditing(Notification)](./nsobject-swift.class/textstoragedidprocessediting%28_%29.md)
- [func textStorageWillProcessEditing(Notification)](./nsobject-swift.class/textstoragewillprocessediting%28_%29.md)
- [func takeStoredValue(Any?, forKey: String)](./nsobject-swift.class/takestoredvalue%28_,forkey%29.md)
  Sets the value of the property identified by a given key.
- [func takeValue(Any?, forKey: String)](./nsobject-swift.class/takevalue%28_,forkey%29.md)
  Sets the value for the property identified by `key` to `value`.
- [func takeValue(Any?, forKeyPath: String)](./nsobject-swift.class/takevalue%28_,forkeypath%29.md)
  Sets the value for the property identified by `keyPath` to `value`.
- [func takeValues(from: [AnyHashable : Any])](./nsobject-swift.class/takevalues%28from%29.md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties
- [func unableToSetNil(forKey: String)](./nsobject-swift.class/unabletosetnil%28forkey%29.md)
  Invoked if `key` is represented by a scalar attribute.
- [func values(forKeys: [Any]) -> [AnyHashable : Any]](./nsobject-swift.class/values%28forkeys%29.md)
  Returns a dictionary containing as keys the property names in `keys`, with corresponding values being the corresponding property values.
- [func workflowController(AMWorkflowController, didError: any Error)](../Automator/amworkflowcontrollerdelegate/workflowcontroller%28_,diderror%29.md)
  Notifies the delegate when the workflow encounters an error.
- [func workflowController(AMWorkflowController, didRun: AMAction)](../Automator/amworkflowcontrollerdelegate/workflowcontroller%28_,didrun%29.md)
  Notifies the delegate when the specified action finishes running.
- [func workflowController(AMWorkflowController, willRun: AMAction)](../Automator/amworkflowcontrollerdelegate/workflowcontroller%28_,willrun%29.md)
  Notifies the delegate when the specified action is about to run.
- [func workflowControllerDidRun(AMWorkflowController)](../Automator/amworkflowcontrollerdelegate/workflowcontrollerdidrun%28_%29.md)
  Notifies the delegate when the workflow controller object finishes running.
- [func workflowControllerDidStop(AMWorkflowController)](../Automator/amworkflowcontrollerdelegate/workflowcontrollerdidstop%28_%29.md)
  Tells the delegate that the workflow controller object has stopped.
- [func workflowControllerWillRun(AMWorkflowController)](../Automator/amworkflowcontrollerdelegate/workflowcontrollerwillrun%28_%29.md)
  Notifies the delegate when the workflow controller object is about to run.
- [func workflowControllerWillStop(AMWorkflowController)](../Automator/amworkflowcontrollerdelegate/workflowcontrollerwillstop%28_%29.md)
  Tells the delegate that the workflow controller object is about to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/deprecated-symbols)*