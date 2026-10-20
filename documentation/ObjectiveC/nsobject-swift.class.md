# NSObject

**Framework**: Objective-C Runtime  
**Kind**: class  
**Role**: Class

The root class of most Objective-C class hierarchies, from which subclasses inherit a basic interface to the runtime system and the ability to behave as Objective-C objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class NSObject
```

```objc
@interface NSObject
```

## Topics

### Initializing a Class
- [class func initialize()](./nsobject-swift.class/initialize%28%29.md)
  Initializes the class before it receives its first message.
- [class func load()](./nsobject-swift.class/load%28%29.md)
  Invoked whenever a class or category is added to the Objective-C runtime; implement this method to perform class-specific behavior upon loading.
### Creating, Copying, and Deallocating Objects
- [init()](./nsobject-swift.class/init%28%29.md)
  Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [func copy() -> Any](./nsobject-swift.class/copy%28%29.md)
  Returns the object returned by `copy(with:)`.
- [func mutableCopy() -> Any](./nsobject-swift.class/mutablecopy%28%29.md)
  Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
### Identifying Classes
- [class func superclass() -> AnyClass?](./nsobject-swift.class/superclass%28%29.md)
  Returns the class object for the receiver’s superclass.
- [class func isSubclass(of: AnyClass) -> Bool](./nsobject-swift.class/issubclass%28of%29.md)
  Returns a Boolean value that indicates whether the receiving class is a subclass of, or identical to, a given class.
### Testing Class Functionality
- [class func instancesRespond(to: Selector!) -> Bool](./nsobject-swift.class/instancesrespond%28to%29.md)
  Returns a Boolean value that indicates whether instances of the receiver are capable of responding to a given selector.
### Testing Protocol Conformance
- [class func conforms(to: Protocol) -> Bool](./nsobject-swift.class/conforms%28to%29.md)
  Returns a Boolean value that indicates whether the target conforms to a given protocol.
### Obtaining Information About Methods
- [func method(for: Selector!) -> IMP!](./nsobject-swift.class/method%28for%29.md)
  Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.
- [class func instanceMethod(for: Selector!) -> IMP!](./nsobject-swift.class/instancemethod%28for%29.md)
  Locates and returns the address of the implementation of the instance method identified by a given selector.
### Describing Objects
- [class func description() -> String](./nsobject-swift.class/description%28%29.md)
  Returns a string that represents the contents of the receiving class.
### Supporting Discardable Content
- [var autoContentAccessingProxy: Any](./nsobject-swift.class/autocontentaccessingproxy.md)
  A proxy for the receiving object
### Sending Messages
- [func perform(Selector, with: Any?, afterDelay: TimeInterval)](./nsobject-swift.class/perform%28_,with,afterdelay%29.md)
  Invokes a method of the receiver on the current thread using the default mode after a delay.
- [func perform(Selector, with: Any?, afterDelay: TimeInterval, inModes: [RunLoop.Mode])](./nsobject-swift.class/perform%28_,with,afterdelay,inmodes%29.md)
  Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [func performSelector(onMainThread: Selector, with: Any?, waitUntilDone: Bool)](./nsobject-swift.class/performselector%28onmainthread,with,waituntildone%29.md)
  Invokes a method of the receiver on the main thread using the default mode.
- [func performSelector(onMainThread: Selector, with: Any?, waitUntilDone: Bool, modes: [String]?)](./nsobject-swift.class/performselector%28onmainthread,with,waituntildone,modes%29.md)
  Invokes a method of the receiver on the main thread using the specified modes.
- [func perform(Selector, on: Thread, with: Any?, waitUntilDone: Bool)](./nsobject-swift.class/perform%28_,on,with,waituntildone%29.md)
  Invokes a method of the receiver on the specified thread using the default mode.
- [func perform(Selector, on: Thread, with: Any?, waitUntilDone: Bool, modes: [String]?)](./nsobject-swift.class/perform%28_,on,with,waituntildone,modes%29.md)
  Invokes a method of the receiver on the specified thread using the specified modes.
- [func performSelector(inBackground: Selector, with: Any?)](./nsobject-swift.class/performselector%28inbackground,with%29.md)
  Invokes a method of the receiver on a new background thread.
- [class func cancelPreviousPerformRequests(withTarget: Any)](./nsobject-swift.class/cancelpreviousperformrequests%28withtarget%29.md)
  Cancels perform requests previously registered with the [`perform(_:with:afterDelay:)`](./nsobject-swift.class/perform%28_,with,afterdelay%29.md) instance method.
- [class func cancelPreviousPerformRequests(withTarget: Any, selector: Selector, object: Any?)](./nsobject-swift.class/cancelpreviousperformrequests%28withtarget,selector,object%29.md)
  Cancels perform requests previously registered with [`perform(_:with:afterDelay:)`](./nsobject-swift.class/perform%28_,with,afterdelay%29.md).
### Forwarding Messages
- [func forwardingTarget(for: Selector!) -> Any?](./nsobject-swift.class/forwardingtarget%28for%29.md)
  Returns the object to which unrecognized messages should first be directed.
### Dynamically Resolving Methods
- [class func resolveClassMethod(Selector!) -> Bool](./nsobject-swift.class/resolveclassmethod%28_%29.md)
  Dynamically provides an implementation for a given selector for a class method.
- [class func resolveInstanceMethod(Selector!) -> Bool](./nsobject-swift.class/resolveinstancemethod%28_%29.md)
  Dynamically provides an implementation for a given selector for an instance method.
### Handling Errors
- [func doesNotRecognizeSelector(Selector!)](./nsobject-swift.class/doesnotrecognizeselector%28_%29.md)
  Handles messages the receiver doesn’t recognize.
### Archiving
- [func awakeAfter(using: NSCoder) -> Any?](./nsobject-swift.class/awakeafter%28using%29.md)
  Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.
- [var classForArchiver: AnyClass?](./nsobject-swift.class/classforarchiver.md)
  The class to substitute for the receiver’s own class during archiving.
- [var classForCoder: AnyClass](./nsobject-swift.class/classforcoder.md)
  Overridden by subclasses to substitute a class other than its own during coding.
- [var classForKeyedArchiver: AnyClass?](./nsobject-swift.class/classforkeyedarchiver.md)
  Subclasses to substitute a new class for instances during keyed archiving.
- [class func classFallbacksForKeyedArchiver() -> [String]](./nsobject-swift.class/classfallbacksforkeyedarchiver%28%29.md)
  Overridden to return the names of classes that can be used to decode objects if their class is unavailable.
- [class func classForKeyedUnarchiver() -> AnyClass](./nsobject-swift.class/classforkeyedunarchiver%28%29.md)
  Overridden by subclasses to substitute a new class during keyed unarchiving.
- [func replacementObject(for: NSArchiver) -> Any?](./nsobject-swift.class/replacementobject%28for%29-8ih2x.md)
  Overridden by subclasses to substitute another object for itself during archiving.
- [func replacementObject(for: NSCoder) -> Any?](./nsobject-swift.class/replacementobject%28for%29-2l8ox.md)
  Overridden by subclasses to substitute another object for itself during encoding.
- [func replacementObject(for: NSKeyedArchiver) -> Any?](./nsobject-swift.class/replacementobject%28for%29-60vwc.md)
  Overridden by subclasses to substitute another object for itself during keyed archiving.
- [class func setVersion(Int)](./nsobject-swift.class/setversion%28_%29.md)
  Sets the receiver’s version number.
- [class func version() -> Int](./nsobject-swift.class/version%28%29.md)
  Returns the version number assigned to the class.
### Working with Class Descriptions
- [var attributeKeys: [String]](./nsobject-swift.class/attributekeys.md)
  An array of `NSString` objects containing the names of immutable values that instances of the receiver’s class contain.
- [var classDescription: NSClassDescription](./nsobject-swift.class/classdescription.md)
  An object containing information about the attributes and relationships of the receiver’s class.
- [func inverse(forRelationshipKey: String) -> String?](./nsobject-swift.class/inverse%28forrelationshipkey%29.md)
  For a given key that defines the name of the relationship from the receiver’s class to another class, returns the name of the relationship from the other class to the receiver’s class.
- [var toManyRelationshipKeys: [String]](./nsobject-swift.class/tomanyrelationshipkeys.md)
  An array containing the keys for the to-many relationship properties of the receiver.
- [var toOneRelationshipKeys: [String]](./nsobject-swift.class/toonerelationshipkeys.md)
  The keys for the to-one relationship properties of the receiver, if any.
### Improving Accessibility
- [UIAccessibility](../UIKit/uiaccessibility-protocol.md)
  A set of methods that provides accessibility information about views and controls in an app’s user interface.
- [UIAccessibilityContainer](../UIKit/uiaccessibilitycontainer.md)
  Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [UIAccessibilityAction](./uiaccessibilityaction.md)
  A set of methods that accessibility elements can use to support specific actions.
- [UIAccessibilityFocus](./uiaccessibilityfocus.md)
  An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [UIAccessibilityDragging](./uiaccessibilitydragging.md)
  A pair of properties to allow you to fine-tune how drags and drops are exposed to assistive technologies.
### Improving browser accessibility
- [func browserAccessibilityAttributedValue(in: NSRange) -> NSAttributedString](./nsobject-swift.class/browseraccessibilityattributedvalue%28in%29.md)
  Returns the value for this element within the given range, as an attributed string.
- [func browserAccessibilityDeleteTextAtCursor(numberOfCharacters: Int)](./nsobject-swift.class/browseraccessibilitydeletetextatcursor%28numberofcharacters%29.md)
  Deletes text from the element at the current cursor position.
- [func browserAccessibilityInsertTextAtCursor(text: String)](./nsobject-swift.class/browseraccessibilityinserttextatcursor%28text%29.md)
  Inserts text into the element at the current cursor position.
- [func browserAccessibilitySelectedTextRange() -> NSRange](./nsobject-swift.class/browseraccessibilityselectedtextrange%28%29.md)
  Returns the range of selected text in the element.
- [func browserAccessibilitySetSelectedTextRange(NSRange)](./nsobject-swift.class/browseraccessibilitysetselectedtextrange%28_%29.md)
  Updates the element’s selected text.
- [func browserAccessibilityValue(in: NSRange) -> String](./nsobject-swift.class/browseraccessibilityvalue%28in%29.md)
  Returns this element’s value in the given range.
- [var browserAccessibilityContainerType: BEAccessibilityContainerType](./nsobject-swift.class/browseraccessibilitycontainertype.md)
  The kind of container that contains this element.
- [var browserAccessibilityCurrentStatus: String?](./nsobject-swift.class/browseraccessibilitycurrentstatus.md)
  A string that’s the element’s value for aria-current.
- [var browserAccessibilityHasDOMFocus: Bool](./nsobject-swift.class/browseraccessibilityhasdomfocus.md)
  A Boolean value that indicates whether the element has native focus in the browser Document Object Model.
- [var browserAccessibilityIsRequired: Bool](./nsobject-swift.class/browseraccessibilityisrequired.md)
  A Boolean value that’s the element’s value for aria-required.
- [var browserAccessibilityPressedState: BEAccessibilityPressedState](./nsobject-swift.class/browseraccessibilitypressedstate.md)
  The element’s value for aria-pressed.
- [var browserAccessibilityRoleDescription: String?](./nsobject-swift.class/browseraccessibilityroledescription.md)
  A string that describes the element’s role for assistive technologies.
- [var browserAccessibilitySortDirection: String?](./nsobject-swift.class/browseraccessibilitysortdirection.md)
  A string that’s the element’s value for aria-sort.
### Scripting
- [var classCode: FourCharCode](./nsobject-swift.class/classcode.md)
  The receiver’s Apple event type code, as stored in the `NSScriptClassDescription` object for the object’s class.
- [var className: String](./nsobject-swift.class/classname.md)
  A string containing the name of the class.
- [func copyScriptingValue(Any, forKey: String, withProperties: [String : Any]) -> Any?](./nsobject-swift.class/copyscriptingvalue%28_,forkey,withproperties%29.md)
  Creates and returns one or more scripting objects to be inserted into the specified relationship by copying the passed-in value and setting the properties in the copied object or objects.
- [func newScriptingObject(of: AnyClass, forValueForKey: String, withContentsValue: Any?, properties: [String : Any]) -> Any?](./nsobject-swift.class/newscriptingobject%28of,forvalueforkey,withcontentsvalue,properties%29.md)
  Creates and returns an instance of a scriptable class, setting its contents and properties, for insertion into the relationship identified by the key.
- [var scriptingProperties: [String : Any]?](./nsobject-swift.class/scriptingproperties.md)
  An `NSString`-keyed dictionary of the receiver’s scriptable properties.
- [func scriptingValue(for: NSScriptObjectSpecifier) -> Any?](./nsobject-swift.class/scriptingvalue%28for%29.md)
  Given an object specifier, returns the specified object or objects in the receiving container.
### Integrating with Combine
- [NSObject.KeyValueObservingPublisher](./nsobject-swift.class/keyvalueobservingpublisher.md)
  A Combine publisher that produces a new element whenever the observed value changes.
### Key-Value Observing
- [NSKeyValueObserving](./nskeyvalueobserving.md)
  An informal protocol that objects adopt to be notified of changes to the specified properties of other objects.
### Key-Value Coding
- [NSKeyValueBindingCreation](./nskeyvaluebindingcreation.md)
  A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [NSKeyValueCoding](./nskeyvaluecoding.md)
  A mechanism by which you can access the properties of an object indirectly by name or key.
- [NSScriptKeyValueCoding](./nsscriptkeyvaluecoding.md)
  A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptKeyValueCoding Exception Names](./nsscriptkeyvaluecoding-exception-names.md)
  Exceptions raised by key-value coding methods.
### Interacting with Web Plug-ins
- [WebPlugInContainer](./webplugincontainer.md)
  `WebPlugInContainer` is an informal protocol that enables a plug-in to send messages to the application.
- [WebPlugIn](./webplugin.md)
  The `WebPlugIn` informal protocol defines methods that enable interaction between an application using the WebKit framework and any WebKit-based plug-ins it may use.
### Implementing Web Scripting
- [WebScripting](./webscripting.md)
  `WebScripting` is an informal protocol that defines methods that classes can implement to export their interfaces to a WebScript environment such as JavaScript.
### Supporting Cocoa Scripting
- [NSScriptingComparisonMethods](./nsscriptingcomparisonmethods.md)
  A collection of methods useful for comparing script objects.
### Customizing accessibility
- [var accessibilityElements: [Any]?](./nsobject-swift.class/accessibilityelements.md)
  An array of features of an object that assistive technologies can access.
### Deprecated
- [Deprecated Symbols](./deprecated-symbols.md)
  Review symbols that are no longer supported and find the replacements to use instead.
### Instance Properties
- [var accessibilityActivateBlock: AXBoolReturnBlock?](./nsobject-swift.class/accessibilityactivateblock.md)
- [var accessibilityActivationPoint: CGPoint](./nsobject-swift.class/accessibilityactivationpoint.md)
- [var accessibilityActivationPointBlock: AXPointReturnBlock?](./nsobject-swift.class/accessibilityactivationpointblock.md)
- [var accessibilityAttributedHint: NSAttributedString?](./nsobject-swift.class/accessibilityattributedhint.md)
- [var accessibilityAttributedHintBlock: AXAttributedStringReturnBlock?](./nsobject-swift.class/accessibilityattributedhintblock.md)
- [var accessibilityAttributedLabel: NSAttributedString?](./nsobject-swift.class/accessibilityattributedlabel.md)
- [var accessibilityAttributedLabelBlock: AXAttributedStringReturnBlock?](./nsobject-swift.class/accessibilityattributedlabelblock.md)
- [var accessibilityAttributedUserInputLabels: [NSAttributedString]!](./nsobject-swift.class/accessibilityattributeduserinputlabels.md)
- [var accessibilityAttributedUserInputLabelsBlock: AXAttributedStringArrayReturnBlock?](./nsobject-swift.class/accessibilityattributeduserinputlabelsblock.md)
- [var accessibilityAttributedValue: NSAttributedString?](./nsobject-swift.class/accessibilityattributedvalue.md)
- [var accessibilityAttributedValueBlock: AXAttributedStringReturnBlock?](./nsobject-swift.class/accessibilityattributedvalueblock.md)
- [var accessibilityContainerType: UIAccessibilityContainerType](./nsobject-swift.class/accessibilitycontainertype.md)
- [var accessibilityContainerTypeBlock: AXContainerTypeReturnBlock?](./nsobject-swift.class/accessibilitycontainertypeblock.md)
- [var accessibilityCustomActionsBlock: AXCustomActionsReturnBlock?](./nsobject-swift.class/accessibilitycustomactionsblock.md)
- [var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?](./nsobject-swift.class/accessibilitycustomrotors.md)
- [var accessibilityCustomRotorsBlock: AXCustomRotorsReturnBlock?](./nsobject-swift.class/accessibilitycustomrotorsblock.md)
- [var accessibilityDecrementBlock: AXVoidReturnBlock?](./nsobject-swift.class/accessibilitydecrementblock.md)
- [var accessibilityDirectTouchOptions: UIAccessibility.DirectTouchOptions](./nsobject-swift.class/accessibilitydirecttouchoptions.md)
- [var accessibilityElementsBlock: AXArrayReturnBlock?](./nsobject-swift.class/accessibilityelementsblock.md)
- [var accessibilityElementsHidden: Bool](./nsobject-swift.class/accessibilityelementshidden.md)
- [var accessibilityElementsHiddenBlock: AXBoolReturnBlock?](./nsobject-swift.class/accessibilityelementshiddenblock.md)
- [var accessibilityExpandedStatus: UIAccessibility.ExpandedStatus](./nsobject-swift.class/accessibilityexpandedstatus.md)
- [var accessibilityExpandedStatusBlock: (() -> UIAccessibility.ExpandedStatus)?](./nsobject-swift.class/accessibilityexpandedstatusblock.md)
- [var accessibilityFocusedUIElement: Any?](./nsobject-swift.class/accessibilityfocuseduielement.md)
- [var accessibilityFrame: CGRect](./nsobject-swift.class/accessibilityframe.md)
- [var accessibilityFrameBlock: AXRectReturnBlock?](./nsobject-swift.class/accessibilityframeblock.md)
- [var accessibilityHeaderElements: [Any]?](./nsobject-swift.class/accessibilityheaderelements.md)
- [var accessibilityHeaderElementsBlock: AXArrayReturnBlock?](./nsobject-swift.class/accessibilityheaderelementsblock.md)
- [var accessibilityHint: String?](./nsobject-swift.class/accessibilityhint.md)
- [var accessibilityHintBlock: AXStringReturnBlock?](./nsobject-swift.class/accessibilityhintblock.md)
- [var accessibilityIdentifierBlock: AXStringReturnBlock?](./nsobject-swift.class/accessibilityidentifierblock.md)
- [var accessibilityIncrementBlock: AXVoidReturnBlock?](./nsobject-swift.class/accessibilityincrementblock.md)
- [var accessibilityLabel: String?](./nsobject-swift.class/accessibilitylabel.md)
- [var accessibilityLabelBlock: AXStringReturnBlock?](./nsobject-swift.class/accessibilitylabelblock.md)
- [var accessibilityLanguage: String?](./nsobject-swift.class/accessibilitylanguage.md)
- [var accessibilityLanguageBlock: AXStringReturnBlock?](./nsobject-swift.class/accessibilitylanguageblock.md)
- [var accessibilityMagicTapBlock: AXBoolReturnBlock?](./nsobject-swift.class/accessibilitymagictapblock.md)
- [var accessibilityNavigationStyle: UIAccessibilityNavigationStyle](./nsobject-swift.class/accessibilitynavigationstyle.md)
- [var accessibilityNavigationStyleBlock: AXNavigationStyleReturnBlock?](./nsobject-swift.class/accessibilitynavigationstyleblock.md)
- [var accessibilityNextTextNavigationElement: Any?](./nsobject-swift.class/accessibilitynexttextnavigationelement.md)
  An accessibility element that contains text that semantically follows this element’s text.
- [var accessibilityNextTextNavigationElementBlock: AXObjectReturnBlock?](./nsobject-swift.class/accessibilitynexttextnavigationelementblock.md)
- [var accessibilityNotifiesWhenDestroyed: Bool](./nsobject-swift.class/accessibilitynotifieswhendestroyed.md)
  A Boolean value that indicates whether a custom accessibility object sends a notification when its corresponding UI element is destroyed.
- [var accessibilityPath: UIBezierPath?](./nsobject-swift.class/accessibilitypath.md)
- [var accessibilityPathBlock: AXPathReturnBlock?](./nsobject-swift.class/accessibilitypathblock.md)
- [var accessibilityPerformEscapeBlock: AXBoolReturnBlock?](./nsobject-swift.class/accessibilityperformescapeblock.md)
- [var accessibilityPreviousTextNavigationElement: Any?](./nsobject-swift.class/accessibilityprevioustextnavigationelement.md)
  An accessibility element that contains text that is semantically previous to this element’s text.
- [var accessibilityPreviousTextNavigationElementBlock: AXObjectReturnBlock?](./nsobject-swift.class/accessibilityprevioustextnavigationelementblock.md)
- [var accessibilityRespondsToUserInteraction: Bool](./nsobject-swift.class/accessibilityrespondstouserinteraction.md)
- [var accessibilityRespondsToUserInteractionBlock: AXBoolReturnBlock?](./nsobject-swift.class/accessibilityrespondstouserinteractionblock.md)
- [var accessibilityShouldGroupAccessibilityChildrenBlock: AXBoolReturnBlock?](./nsobject-swift.class/accessibilityshouldgroupaccessibilitychildrenblock.md)
- [var accessibilityTextInputResponder: (any UITextInput)?](./nsobject-swift.class/accessibilitytextinputresponder.md)
  The object that handles text input calls for this accessibility element.
- [var accessibilityTextInputResponderBlock: AXUITextInputReturnBlock?](./nsobject-swift.class/accessibilitytextinputresponderblock.md)
  The block to use to handle text input calls to a backing view.
- [var accessibilityTextualContext: UIAccessibilityTextualContext?](./nsobject-swift.class/accessibilitytextualcontext.md)
- [var accessibilityTextualContextBlock: AXTextualContextReturnBlock?](./nsobject-swift.class/accessibilitytextualcontextblock.md)
- [var accessibilityTraits: UIAccessibilityTraits](./nsobject-swift.class/accessibilitytraits.md)
- [var accessibilityTraitsBlock: AXTraitsReturnBlock?](./nsobject-swift.class/accessibilitytraitsblock.md)
- [var accessibilityUserInputLabels: [String]!](./nsobject-swift.class/accessibilityuserinputlabels.md)
- [var accessibilityUserInputLabelsBlock: AXStringArrayReturnBlock?](./nsobject-swift.class/accessibilityuserinputlabelsblock.md)
- [var accessibilityValue: String?](./nsobject-swift.class/accessibilityvalue.md)
- [var accessibilityValueBlock: AXStringReturnBlock?](./nsobject-swift.class/accessibilityvalueblock.md)
- [var accessibilityViewIsModal: Bool](./nsobject-swift.class/accessibilityviewismodal.md)
- [var accessibilityViewIsModalBlock: AXBoolReturnBlock?](./nsobject-swift.class/accessibilityviewismodalblock.md)
- [var automationElements: [Any]?](./nsobject-swift.class/automationelements.md)
- [var automationElementsBlock: AXArrayReturnBlock?](./nsobject-swift.class/automationelementsblock.md)
- [var browserAccessibilityDetailsElements: [NSObject]](./nsobject-swift.class/browseraccessibilitydetailselements.md)
- [var browserAccessibilityImageDataSize: CGSize](./nsobject-swift.class/browseraccessibilityimagedatasize-swift.property.md)
  Returns the native pixel dimensions of the image represented by this element, or `CGSize.zero` if this element does not represent an image.
- [var browserAccessibilityKeyboardShortcuts: String?](./nsobject-swift.class/browseraccessibilitykeyboardshortcuts.md)
- [var browserAccessibilityOrientation: BEAccessibilityOrientation](./nsobject-swift.class/browseraccessibilityorientation.md)
- [var isAccessibilityElement: Bool](./nsobject-swift.class/isaccessibilityelement.md)
- [var isAccessibilityElementBlock: AXBoolReturnBlock?](./nsobject-swift.class/isaccessibilityelementblock.md)
- [var isSelectable: Bool](./nsobject-swift.class/isselectable.md)
- [var objectSpecifier: NSScriptObjectSpecifier?](./nsobject-swift.class/objectspecifier.md)
  Returns an object specifier for the receiver.
- [var shouldGroupAccessibilityChildren: Bool](./nsobject-swift.class/shouldgroupaccessibilitychildren.md)
### Instance Methods
- [func acceptsPreviewPanelControl(QLPreviewPanel!) -> Bool](./nsobject-swift.class/acceptspreviewpanelcontrol%28_%29.md)
- [func accessibilityElement(at: Int) -> Any?](./nsobject-swift.class/accessibilityelement%28at%29.md)
- [func accessibilityElementCount() -> Int](./nsobject-swift.class/accessibilityelementcount%28%29.md)
- [func accessibilityHitTest(NSPoint) -> Any?](./nsobject-swift.class/accessibilityhittest%28_%29.md)
- [func accessibilityHitTest(CGPoint, event: UIEvent?) -> Any?](./nsobject-swift.class/accessibilityhittest%28_,event%29.md)
- [func accessibilityLineEndPositionFromCurrentSelection() -> Int](./nsobject-swift.class/accessibilitylineendpositionfromcurrentselection%28%29.md)
- [func accessibilityLineRange(forPosition: Int) -> NSRange](./nsobject-swift.class/accessibilitylinerange%28forposition%29.md)
- [func accessibilityLineStartPositionFromCurrentSelection() -> Int](./nsobject-swift.class/accessibilitylinestartpositionfromcurrentselection%28%29.md)
- [func accessibilityZoomIn(at: CGPoint) -> Bool](./nsobject-swift.class/accessibilityzoomin%28at%29.md)
  Zooms in on the content at the specified point.
- [func accessibilityZoomOut(at: CGPoint) -> Bool](./nsobject-swift.class/accessibilityzoomout%28at%29.md)
  Zooms out from the content at the specified point.
- [func actionProperty() -> String!](./nsobject-swift.class/actionproperty%28%29.md)
  Sent to the delegate to request the property the action applies to.
- [func attemptRecovery(fromError: any Error, optionIndex: Int) -> Bool](./nsobject-swift.class/attemptrecovery%28fromerror,optionindex%29.md)
  Implemented to attempt a recovery from an error noted in an application-modal dialog.
- [func attemptRecovery(fromError: any Error, optionIndex: Int, delegate: Any?, didRecoverSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)](./nsobject-swift.class/attemptrecovery%28fromerror,optionindex,delegate,didrecoverselector,contextinfo%29.md)
  Implemented to attempt a recovery from an error noted in a document-modal sheet.
- [func authorizationViewCreatedAuthorization(SFAuthorizationView!)](./nsobject-swift.class/authorizationviewcreatedauthorization%28_%29.md)
  Sent to the delegate to indicate the authorization object has been created or changed.
- [func authorizationViewDidAuthorize(SFAuthorizationView!)](./nsobject-swift.class/authorizationviewdidauthorize%28_%29.md)
  Sent to the delegate to indicate the user was authorized and the authorization view was changed to unlocked.
- [func authorizationViewDidDeauthorize(SFAuthorizationView!)](./nsobject-swift.class/authorizationviewdiddeauthorize%28_%29.md)
  Sent to the delegate to indicate the user was deauthorized and the authorization view was changed to locked.
- [func authorizationViewDidHide(SFAuthorizationView!)](./nsobject-swift.class/authorizationviewdidhide%28_%29.md)
  Sent to the delegate to indicate that the view’s visibility has changed.
- [func authorizationViewReleasedAuthorization(SFAuthorizationView!)](./nsobject-swift.class/authorizationviewreleasedauthorization%28_%29.md)
  Sent to the delegate to indicate that deauthorization is about to occur.
- [func authorizationViewShouldDeauthorize(SFAuthorizationView!) -> Bool](./nsobject-swift.class/authorizationviewshoulddeauthorize%28_%29.md)
  Sent to the delegate when a user clicks the open lock icon.
- [func awakeFromNib()](./nsobject-swift.class/awakefromnib%28%29.md)
  Prepares the receiver for service after it has been loaded from an Interface Builder archive, or nib file.
- [func beginPreviewPanelControl(QLPreviewPanel!)](./nsobject-swift.class/beginpreviewpanelcontrol%28_%29.md)
- [func browserAccessibilityImageData([AnyHashable : Any]) -> CVPixelBuffer?](./nsobject-swift.class/browseraccessibilityimagedata%28_%29.md)
- [func burnProgressPanel(DRBurnProgressPanel!, burnDidFinish: DRBurn!) -> Bool](./nsobject-swift.class/burnprogresspanel%28_,burndidfinish%29.md)
  Allows the delegate to handle the end-of-burn feedback.
- [func burnProgressPanelDidFinish(Notification!)](./nsobject-swift.class/burnprogresspaneldidfinish%28_%29.md)
  Notification sent by the panel after ordering out.
- [func burnProgressPanelWillBegin(Notification!)](./nsobject-swift.class/burnprogresspanelwillbegin%28_%29.md)
  Notification sent by the panel before display.
- [func candidates(Any!) -> [Any]!](./nsobject-swift.class/candidates%28_%29.md)
  Returns an array of candidates.
- [func certificatePanelShowHelp(SFCertificatePanel!) -> Bool](./nsobject-swift.class/certificatepanelshowhelp%28_%29.md)
  Implements custom help behavior for the modal panel.
- [func chooseIdentityPanelShowHelp(SFChooseIdentityPanel!) -> Bool](./nsobject-swift.class/chooseidentitypanelshowhelp%28_%29.md)
  Implements custom help behavior for the modal panel.
- [func commitComposition(Any!)](./nsobject-swift.class/commitcomposition%28_%29.md)
  Informs the controller that the composition should be committed.
- [func composedString(Any!) -> Any!](./nsobject-swift.class/composedstring%28_%29.md)
  Return the current composed string.
- [func compositionParameterView(QCCompositionParameterView!, didChangeParameterWithKey: String!)](./nsobject-swift.class/compositionparameterview%28_,didchangeparameterwithkey%29.md)
  Called after an input parameter in the composition parameter view has been edited.
- [func compositionParameterView(QCCompositionParameterView!, shouldDisplayParameterWithKey: String!, attributes: [AnyHashable : Any]!) -> Bool](./nsobject-swift.class/compositionparameterview%28_,shoulddisplayparameterwithkey,attributes%29.md)
  Allows you to define which composition parameters are visible in the user interface when the composition parameter view refreshes.
- [func compositionPickerView(QCCompositionPickerView!, didSelect: QCComposition!)](./nsobject-swift.class/compositionpickerview%28_,didselect%29.md)
  Performs custom tasks when the selected composition in the composition picker view changes.
- [func compositionPickerViewDidStartAnimating(QCCompositionPickerView!)](./nsobject-swift.class/compositionpickerviewdidstartanimating%28_%29.md)
  Performs custom tasks when the composition picker view starts animating a composition.
- [func compositionPickerViewWillStopAnimating(QCCompositionPickerView!)](./nsobject-swift.class/compositionpickerviewwillstopanimating%28_%29.md)
  Performs custom tasks when the composition picker view stops animating a composition.
- [func didCommand(by: Selector!, client: Any!) -> Bool](./nsobject-swift.class/didcommand%28by,client%29.md)
  Processes a command  generated by user action such as typing certain keys or pressing the mouse button.
- [func doesContain(Any) -> Bool](./nsobject-swift.class/doescontain%28_%29.md)
  Returns a Boolean value that indicates whether the receiver contains a given object.
- [func endPreviewPanelControl(QLPreviewPanel!)](./nsobject-swift.class/endpreviewpanelcontrol%28_%29.md)
- [func eraseProgressPanel(DREraseProgressPanel!, eraseDidFinish: DRErase!) -> Bool](./nsobject-swift.class/eraseprogresspanel%28_,erasedidfinish%29.md)
  Notification sent by the panel before display.
- [func eraseProgressPanelDidFinish(Notification!)](./nsobject-swift.class/eraseprogresspaneldidfinish%28_%29.md)
  Notification sent by the panel after ordering out.
- [func eraseProgressPanelWillBegin(Notification!)](./nsobject-swift.class/eraseprogresspanelwillbegin%28_%29.md)
  Notification sent by the panel before display.
- [func exceptionHandler(NSExceptionHandler!, shouldHandle: NSException!, mask: Int) -> Bool](./nsobject-swift.class/exceptionhandler%28_,shouldhandle,mask%29.md)
  Implemented by the delegate to evaluate whether the delegating exception handler should handle a given exception.
- [func exceptionHandler(NSExceptionHandler!, shouldLogException: NSException!, mask: Int) -> Bool](./nsobject-swift.class/exceptionhandler%28_,shouldlogexception,mask%29.md)
  Implemented by the delegate to evaluate whether the delegating exception hangler should log a given exception.
- [func fileTransferServicesAbortComplete(OBEXFileTransferServices!, error: OBEXError)](./nsobject-swift.class/filetransferservicesabortcomplete%28_,error%29.md)
- [func fileTransferServicesConnectionComplete(OBEXFileTransferServices!, error: OBEXError)](./nsobject-swift.class/filetransferservicesconnectioncomplete%28_,error%29.md)
- [func fileTransferServicesCopyRemoteFileComplete(OBEXFileTransferServices!, error: OBEXError)](./nsobject-swift.class/filetransferservicescopyremotefilecomplete%28_,error%29.md)
- [func fileTransferServicesCopyRemoteFileProgress(OBEXFileTransferServices!, transferProgress: [AnyHashable : Any]!)](./nsobject-swift.class/filetransferservicescopyremotefileprogress%28_,transferprogress%29.md)
- [func fileTransferServicesCreateFolderComplete(OBEXFileTransferServices!, error: OBEXError, folder: String!)](./nsobject-swift.class/filetransferservicescreatefoldercomplete%28_,error,folder%29.md)
- [func fileTransferServicesDisconnectionComplete(OBEXFileTransferServices!, error: OBEXError)](./nsobject-swift.class/filetransferservicesdisconnectioncomplete%28_,error%29.md)
- [func fileTransferServicesFilePreparationComplete(OBEXFileTransferServices!, error: OBEXError)](./nsobject-swift.class/filetransferservicesfilepreparationcomplete%28_,error%29.md)
- [func fileTransferServicesPathChangeComplete(OBEXFileTransferServices!, error: OBEXError, finalPath: String!)](./nsobject-swift.class/filetransferservicespathchangecomplete%28_,error,finalpath%29.md)
- [func fileTransferServicesRemoveItemComplete(OBEXFileTransferServices!, error: OBEXError, removedItem: String!)](./nsobject-swift.class/filetransferservicesremoveitemcomplete%28_,error,removeditem%29.md)
- [func fileTransferServicesRetrieveFolderListingComplete(OBEXFileTransferServices!, error: OBEXError, listing: [Any]!)](./nsobject-swift.class/filetransferservicesretrievefolderlistingcomplete%28_,error,listing%29.md)
- [func fileTransferServicesSendFileComplete(OBEXFileTransferServices!, error: OBEXError)](./nsobject-swift.class/filetransferservicessendfilecomplete%28_,error%29.md)
- [func fileTransferServicesSendFileProgress(OBEXFileTransferServices!, transferProgress: [AnyHashable : Any]!)](./nsobject-swift.class/filetransferservicessendfileprogress%28_,transferprogress%29.md)
- [func handle(NSEvent!, client: Any!) -> Bool](./nsobject-swift.class/handle%28_,client%29.md)
  Handles key down and mouse events.
- [func imageBrowser(IKImageBrowserView!, backgroundWasRightClickedWith: NSEvent!)](./nsobject-swift.class/imagebrowser%28_,backgroundwasrightclickedwith%29.md)
  Performs custom tasks when the user right-clicks the image browser view background.
- [func imageBrowser(IKImageBrowserView!, cellWasDoubleClickedAt: Int)](./nsobject-swift.class/imagebrowser%28_,cellwasdoubleclickedat%29.md)
  Performs custom tasks when the user double-clicks an item in the image browser view.
- [func imageBrowser(IKImageBrowserView!, cellWasRightClickedAt: Int, with: NSEvent!)](./nsobject-swift.class/imagebrowser%28_,cellwasrightclickedat,with%29.md)
  Performs custom tasks when the user right-clicks an item in the image browser view.
- [func imageBrowser(IKImageBrowserView!, groupAt: Int) -> [AnyHashable : Any]!](./nsobject-swift.class/imagebrowser%28_,groupat%29.md)
  Returns the group at the specified index.
- [func imageBrowser(IKImageBrowserView!, itemAt: Int) -> Any!](./nsobject-swift.class/imagebrowser%28_,itemat%29.md)
  Returns an object for the item in an image browser view that corresponds to the specified index.
- [func imageBrowser(IKImageBrowserView!, moveItemsAt: IndexSet!, to: Int) -> Bool](./nsobject-swift.class/imagebrowser%28_,moveitemsat,to%29.md)
  Signals that the specified items should be moved to the specified destination.
- [func imageBrowser(IKImageBrowserView!, removeItemsAt: IndexSet!)](./nsobject-swift.class/imagebrowser%28_,removeitemsat%29.md)
  Signals that a remove operation should be applied to the specified items.
- [func imageBrowser(IKImageBrowserView!, writeItemsAt: IndexSet!, to: NSPasteboard!) -> Int](./nsobject-swift.class/imagebrowser%28_,writeitemsat,to%29.md)
  Signals that a drag should begin.
- [func imageBrowserSelectionDidChange(IKImageBrowserView!)](./nsobject-swift.class/imagebrowserselectiondidchange%28_%29.md)
  Performs custom tasks when the selection changes.
- [func imageRepresentation() -> Any!](./nsobject-swift.class/imagerepresentation%28%29.md)
  Returns the image to display.
- [func imageRepresentationType() -> String!](./nsobject-swift.class/imagerepresentationtype%28%29.md)
  Returns the representation type of the image to display.
- [func imageSubtitle() -> String!](./nsobject-swift.class/imagesubtitle%28%29.md)
  Returns the display subtitle of the image.
- [func imageTitle() -> String!](./nsobject-swift.class/imagetitle%28%29.md)
  Returns the display title of the image.
- [func imageUID() -> String!](./nsobject-swift.class/imageuid%28%29.md)
  Returns a unique string that identifies the data source item.
- [func imageVersion() -> Int](./nsobject-swift.class/imageversion%28%29.md)
  Returns the version of the item.
- [func index(ofAccessibilityElement: Any) -> Int](./nsobject-swift.class/index%28ofaccessibilityelement%29.md)
- [func indicesOfObjects(byEvaluatingObjectSpecifier: NSScriptObjectSpecifier) -> [NSNumber]?](./nsobject-swift.class/indicesofobjects%28byevaluatingobjectspecifier%29.md)
  Returns the indices of the specified container objects.
- [func inputText(String!, client: Any!) -> Bool](./nsobject-swift.class/inputtext%28_,client%29.md)
  Handles key down events that do not map to an action method.
- [func inputText(String!, key: Int, modifiers: Int, client: Any!) -> Bool](./nsobject-swift.class/inputtext%28_,key,modifiers,client%29.md)
  Receives Unicode, the key code that generated it, and any modifier flags.
- [func isCaseInsensitiveLike(String) -> Bool](./nsobject-swift.class/iscaseinsensitivelike%28_%29.md)
  Returns a Boolean value that indicates whether receiver is considered to be “like” a given string when the case of characters in the receiver is ignored.
- [func isEqual(to: Any?) -> Bool](./nsobject-swift.class/isequal%28to%29.md)
  Returns a Boolean value that indicates whether the receiver is equal to another given object.
- [func isGreaterThan(Any?) -> Bool](./nsobject-swift.class/isgreaterthan%28_%29.md)
  Returns a Boolean value that indicates whether the receiver is greater than another given object.
- [func isGreaterThanOrEqual(to: Any?) -> Bool](./nsobject-swift.class/isgreaterthanorequal%28to%29.md)
  Returns a Boolean value that indicates whether the receiver is greater than or equal to another given object.
- [func isLessThan(Any?) -> Bool](./nsobject-swift.class/islessthan%28_%29.md)
  Returns a Boolean value that indicates whether the receiver is less than another given object.
- [func isLessThanOrEqual(to: Any?) -> Bool](./nsobject-swift.class/islessthanorequal%28to%29.md)
  Returns a Boolean value that indicates whether the receiver is less than or equal to another given object.
- [func isLike(String) -> Bool](./nsobject-swift.class/islike%28_%29.md)
  Returns a Boolean value that indicates whether the receiver is “like” another given object.
- [func isNotEqual(to: Any?) -> Bool](./nsobject-swift.class/isnotequal%28to%29.md)
  Returns a Boolean value that indicates whether the receiver is not equal to another given object.
- [func numberOfGroups(inImageBrowser: IKImageBrowserView!) -> Int](./nsobject-swift.class/numberofgroups%28inimagebrowser%29.md)
  Returns the number of groups in an image browser view.
- [func numberOfItems(inImageBrowser: IKImageBrowserView!) -> Int](./nsobject-swift.class/numberofitems%28inimagebrowser%29.md)
  Returns the number of records managed by the data source object.
- [func originalString(Any!) -> NSAttributedString!](./nsobject-swift.class/originalstring%28_%29.md)
  Return the string that consists of the precomposed Unicode characters.
- [func performAction(for: ABPerson!, identifier: String!)](./nsobject-swift.class/performaction%28for,identifier%29.md)
  Sent to the delegate to perform the action.
- [func prepareForInterfaceBuilder()](./nsobject-swift.class/prepareforinterfacebuilder%28%29.md)
  Called when a designable object is created in Interface Builder.
- [func provideImage(to: any MTLTexture, commandBuffer: any MTLCommandBuffer, originx: Int, originy: Int, width: Int, height: Int, userInfo: Any?)](./nsobject-swift.class/provideimage%28to,commandbuffer,originx,originy,width,height,userinfo%29.md)
  An optional method that an image provider object may implement.
With this method, the provider object can use the Metal API to provide pixel
data into a MTLTexture when the image object is rendered.
- [func provideImageData(UnsafeMutableRawPointer, bytesPerRow: Int, origin: Int, Int, size: Int, Int, userInfo: Any?)](./nsobject-swift.class/provideimagedata%28_,bytesperrow,origin,_,size,_,userinfo%29.md)
  Supplies data to a `CIImage` object.
- [func quartzFilterManager(QuartzFilterManager!, didAdd: QuartzFilter!)](./nsobject-swift.class/quartzfiltermanager%28_,didadd%29.md)
- [func quartzFilterManager(QuartzFilterManager!, didModifyFilter: QuartzFilter!)](./nsobject-swift.class/quartzfiltermanager%28_,didmodifyfilter%29.md)
- [func quartzFilterManager(QuartzFilterManager!, didRemove: QuartzFilter!)](./nsobject-swift.class/quartzfiltermanager%28_,didremove%29.md)
- [func quartzFilterManager(QuartzFilterManager!, didSelect: QuartzFilter!)](./nsobject-swift.class/quartzfiltermanager%28_,didselect%29.md)
- [func readLinkQuality(forDeviceComplete: Any!, device: IOBluetoothDevice!, info: UnsafeMutablePointer<BluetoothHCILinkQualityInfo>!, error: IOReturn)](./nsobject-swift.class/readlinkquality%28fordevicecomplete,device,info,error%29.md)
- [func readRSSI(forDeviceComplete: Any!, device: IOBluetoothDevice!, info: UnsafeMutablePointer<BluetoothHCIRSSIInfo>!, error: IOReturn)](./nsobject-swift.class/readrssi%28fordevicecomplete,device,info,error%29.md)
- [func saveOptions(IKSaveOptions!, shouldShowUTType: String!) -> Bool](./nsobject-swift.class/saveoptions%28_,shouldshowuttype%29.md)
  Called to determine if the specified uniform type identifier should be shown in the save panel.
- [func setSharedObservers(NSKeyValueSharedObserversSnapshot?)](./nsobject-swift.class/setsharedobservers%28_%29.md)
- [func setupPanel(DRSetupPanel!, determineBestDeviceOfA: DRDevice!, orB: DRDevice!) -> DRDevice!](./nsobject-swift.class/setuppanel%28_,determinebestdeviceofa,orb%29.md)
  Allows the delegate to specify which device is its preferred.
- [func setupPanel(DRSetupPanel!, deviceContainsSuitableMedia: DRDevice!, promptString: AutoreleasingUnsafeMutablePointer<NSString?>!) -> Bool](./nsobject-swift.class/setuppanel%28_,devicecontainssuitablemedia,promptstring%29.md)
  This delegate method allows the delegate to determine if the media inserted in the device is suitable for whatever operation is to be performed.
- [func setupPanel(DRSetupPanel!, deviceCouldBeTarget: DRDevice!) -> Bool](./nsobject-swift.class/setuppanel%28_,devicecouldbetarget%29.md)
  Allows the delegate to determine if device can be used as a target.
- [func setupPanelDeviceSelectionChanged(Notification!)](./nsobject-swift.class/setuppaneldeviceselectionchanged%28_%29.md)
  Sent by the default notification center when the device selection in the panel has changed.
- [func setupPanelShouldHandleMediaReservations(DRSetupPanel!) -> Bool](./nsobject-swift.class/setuppanelshouldhandlemediareservations%28_%29.md)
  This delegate method allows the delegate to control how media reservations are handled.
- [func shouldEnableAction(for: ABPerson!, identifier: String!) -> Bool](./nsobject-swift.class/shouldenableaction%28for,identifier%29.md)
  Sent to the delegate to determine whether the action should be enabled.
- [func title(for: ABPerson!, identifier: String!) -> String!](./nsobject-swift.class/title%28for,identifier%29.md)
  Sent to the delegate to request the title of the menu item for the action.
- [func workflowController(AMWorkflowController, didError: any Error)](./nsobject-swift.class/workflowcontroller%28_,diderror%29.md)
- [func workflowController(AMWorkflowController, didRun: AMAction)](./nsobject-swift.class/workflowcontroller%28_,didrun%29.md)
- [func workflowController(AMWorkflowController, willRun: AMAction)](./nsobject-swift.class/workflowcontroller%28_,willrun%29.md)
- [func workflowControllerDidRun(AMWorkflowController)](./nsobject-swift.class/workflowcontrollerdidrun%28_%29.md)
- [func workflowControllerDidStop(AMWorkflowController)](./nsobject-swift.class/workflowcontrollerdidstop%28_%29.md)
- [func workflowControllerWillRun(AMWorkflowController)](./nsobject-swift.class/workflowcontrollerwillrun%28_%29.md)
- [func workflowControllerWillStop(AMWorkflowController)](./nsobject-swift.class/workflowcontrollerwillstop%28_%29.md)
### Type Methods
- [class func debugDescription() -> String](./nsobject-swift.class/debugdescription%28%29.md)
- [class func hash() -> Int](./nsobject-swift.class/hash%28%29.md)
### Default Implementations
- [Equatable Implementations](./nsobject-swift.class/equatable-implementations.md)
- [Hashable Implementations](./nsobject-swift.class/hashable-implementations.md)

## Relationships

### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](./nsobjectprotocol.md)

## See Also

### Classes
- [class Protocol](./protocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class)*