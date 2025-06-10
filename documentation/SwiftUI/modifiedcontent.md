# ModifiedContent

**Framework**: SwiftUI  
**Kind**: struct

A value with a modifier applied to it.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct ModifiedContent<Content, Modifier>
```

## Topics

### Creating a modified content view
- [init(content: Content, modifier: Modifier)](modifiedcontent/init(content:modifier:).md)
  A structure that defines the content and modifier needed to produce a new view or view modifier.
- [var content: Content](modifiedcontent/content.md)
  The content that the modifier transforms into a new view or new view modifier.
- [var modifier: Modifier](modifiedcontent/modifier.md)
  The view modifier.
### Instance Methods
- [func accessibility(activationPoint:)](modifiedcontent/accessibility(activationpoint:).md)
  Specifies the point where activations occur in the view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibility(addtraits:).md)
  Adds the given traits to the view.
- [func accessibility(hidden: Bool) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(hint: Text) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibility(hint:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(identifier: String) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibility(identifier:).md)
  Uses the specified string to identify the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibility(inputlabels:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(label: Text) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibility(removetraits:).md)
  Removes the given traits from this view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibility(selectionidentifier:).md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibility(sortpriority:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibility(value: Text) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityaction(_:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<I>(AccessibilityActionKind, intent: I) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityaction(_:intent:).md)
  Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction(named:_:)](modifiedcontent/accessibilityaction(named:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named:intent:)](modifiedcontent/accessibilityaction(named:intent:).md)
  Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityActivationPoint(_:)](modifiedcontent/accessibilityactivationpoint(_:).md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(_:isEnabled:)](modifiedcontent/accessibilityactivationpoint(_:isenabled:).md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityaddtraits(_:).md)
  Adds the given traits to the view.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityadjustableaction(_:).md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityCustomContent(_:_:importance:)](modifiedcontent/accessibilitycustomcontent(_:_:importance:).md)
  Add additional accessibility information to the view.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilitydirecttouch(_:options:).md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityDragPoint(_:description:)](modifiedcontent/accessibilitydragpoint(_:description:).md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(_:description:isEnabled:)](modifiedcontent/accessibilitydragpoint(_:description:isenabled:).md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint(_:description:)](modifiedcontent/accessibilitydroppoint(_:description:).md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(_:description:isEnabled:)](modifiedcontent/accessibilitydroppoint(_:description:isenabled:).md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityheading(_:).md)
  Set the level of this heading.
- [func accessibilityHidden(Bool) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityhidden(_:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHidden(Bool, isEnabled: Bool) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityhidden(_:isenabled:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHint(_:)](modifiedcontent/accessibilityhint(_:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(_:isEnabled:)](modifiedcontent/accessibilityhint(_:isenabled:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityIdentifier(String) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityidentifier(_:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityidentifier(_:isenabled:).md)
  Uses the string you specify to identify the view.
- [func accessibilityInputLabels(_:)](modifiedcontent/accessibilityinputlabels(_:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels(_:isEnabled:)](modifiedcontent/accessibilityinputlabels(_:isenabled:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabel(_:)](modifiedcontent/accessibilitylabel(_:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(_:isEnabled:)](modifiedcontent/accessibilitylabel(_:isenabled:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityremovetraits(_:).md)
  Removes the given traits from this view.
- [func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityrespondstouserinteraction(_:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRespondsToUserInteraction(Bool, isEnabled: Bool) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityrespondstouserinteraction(_:isenabled:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityscrollaction(_:).md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollStatus(_:isEnabled:)](modifiedcontent/accessibilityscrollstatus(_:isenabled:).md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilitysortpriority(_:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityValue(_:)](modifiedcontent/accessibilityvalue(_:).md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(_:isEnabled:)](modifiedcontent/accessibilityvalue(_:isenabled:).md)
  Adds a textual description of the value that the view contains.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Content, Modifier>](modifiedcontent/accessibilityzoomaction(_:).md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Chart3DContent](../Charts/Chart3DContent.md)
- [Copyable](../Swift/Copyable.md)
- [CustomHoverEffect](customhovereffect.md)
- [DynamicMapContent](../MapKit/DynamicMapContent.md)
- [DynamicTableRowContent](dynamictablerowcontent.md)
- [DynamicViewContent](dynamicviewcontent.md)
- [Equatable](../Swift/Equatable.md)
- [HoverEffectContent](hovereffectcontent.md)
- [MapContent](../MapKit/MapContent.md)
- [Scene](scene.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TableRowContent](tablerowcontent.md)
- [View](view.md)
- [ViewModifier](viewmodifier.md)
- [VisualEffect](visualeffect.md)

## See Also

- [Configuring views](configuring-views.md)
  Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md)
  Bundle view modifiers that you regularly reuse into a custom view modifier.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](view/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
- [protocol ViewModifier](viewmodifier.md)
  A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [struct EmptyModifier](emptymodifier.md)
  An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [protocol EnvironmentalModifier](environmentalmodifier.md)
  A modifier that must resolve to a concrete modifier in an environment before use.
- [struct ManipulableModifier](manipulablemodifier.md)
- [struct ManipulableResponderModifier](manipulablerespondermodifier.md)
- [struct ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
- [struct ManipulationGeometryModifier](manipulationgeometrymodifier.md)
- [struct ManipulationGestureModifier](manipulationgesturemodifier.md)
- [struct ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
- [enum Manipulable](manipulable.md)
  A namespace for various manipulable related types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/modifiedcontent)*