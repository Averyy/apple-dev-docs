# ModifiedContent

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [init(content: Content, modifier: Modifier)](./modifiedcontent/init%28content,modifier%29.md)
  A structure that defines the content and modifier needed to produce a new view or view modifier.
- [var content: Content](./modifiedcontent/content.md)
  The content that the modifier transforms into a new view or new view modifier.
- [var modifier: Modifier](./modifiedcontent/modifier.md)
  The view modifier.
### Deprecated
- [Deprecated symbols](./modifiedcontent-deprecated.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Instance Methods
- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityaction%28_,_%29.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<I>(AccessibilityActionKind, intent: I) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityaction%28_,intent%29.md)
  Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction(named:_:)](./modifiedcontent/accessibilityaction%28named,_%29.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named:intent:)](./modifiedcontent/accessibilityaction%28named,intent%29.md)
  Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityActivationPoint(_:)](./modifiedcontent/accessibilityactivationpoint%28_%29.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(_:isEnabled:)](./modifiedcontent/accessibilityactivationpoint%28_,isenabled%29.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityaddtraits%28_%29.md)
  Adds the given traits to the view.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityadjustableaction%28_%29.md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityCustomContent(_:_:importance:)](./modifiedcontent/accessibilitycustomcontent%28_,_,importance%29.md)
  Add additional accessibility information to the view.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilitydirecttouch%28_,options%29.md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityDragPoint(_:description:)](./modifiedcontent/accessibilitydragpoint%28_,description%29.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(_:description:isEnabled:)](./modifiedcontent/accessibilitydragpoint%28_,description,isenabled%29.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint(_:description:)](./modifiedcontent/accessibilitydroppoint%28_,description%29.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(_:description:isEnabled:)](./modifiedcontent/accessibilitydroppoint%28_,description,isenabled%29.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityheading%28_%29.md)
  Set the level of this heading.
- [func accessibilityHidden(Bool) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityhidden%28_%29.md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHidden(Bool, isEnabled: Bool) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityhidden%28_,isenabled%29.md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHint(_:)](./modifiedcontent/accessibilityhint%28_%29.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(_:isEnabled:)](./modifiedcontent/accessibilityhint%28_,isenabled%29.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityIdentifier(String) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityidentifier%28_%29.md)
  Uses the string you specify to identify the view.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityidentifier%28_,isenabled%29.md)
  Uses the string you specify to identify the view.
- [func accessibilityInputLabels(_:)](./modifiedcontent/accessibilityinputlabels%28_%29.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels(_:isEnabled:)](./modifiedcontent/accessibilityinputlabels%28_,isenabled%29.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabel(_:)](./modifiedcontent/accessibilitylabel%28_%29.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(_:isEnabled:)](./modifiedcontent/accessibilitylabel%28_,isenabled%29.md)
  Adds a label to the view that describes its contents.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityremovetraits%28_%29.md)
  Removes the given traits from this view.
- [func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityrespondstouserinteraction%28_%29.md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRespondsToUserInteraction(Bool, isEnabled: Bool) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityrespondstouserinteraction%28_,isenabled%29.md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityscrollaction%28_%29.md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollStatus(_:isEnabled:)](./modifiedcontent/accessibilityscrollstatus%28_,isenabled%29.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilitysortpriority%28_%29.md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilitytextcontenttype%28_%29.md)
  Sets an accessibility text content type.
- [func accessibilityValue(_:)](./modifiedcontent/accessibilityvalue%28_%29.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(_:isEnabled:)](./modifiedcontent/accessibilityvalue%28_,isenabled%29.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibilityzoomaction%28_%29.md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.

## Relationships

### Conforms To
- [Animatable](./animatable.md)
- [Chart3DContent](../Charts/chart3dcontent.md)
- [Copyable](../Swift/copyable.md)
- [CustomHoverEffect](./customhovereffect.md)
- [DynamicMapContent](../MapKit/dynamicmapcontent.md)
- [DynamicTableRowContent](./dynamictablerowcontent.md)
- [DynamicViewContent](./dynamicviewcontent.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [HoverEffectContent](./hovereffectcontent.md)
- [MapContent](../MapKit/mapcontent.md)
- [Scene](./scene.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TableRowContent](./tablerowcontent.md)
- [View](./view.md)
- [ViewModifier](./viewmodifier.md)
- [VisualEffect](./visualeffect.md)

## See Also

### Modifying a view
- [Configuring views](./configuring-views.md)
  Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](./reducing-view-modifier-maintenance.md)
  Bundle view modifiers that you regularly reuse into a custom view modifier.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](./view/modifier%28_%29.md)
  Applies a modifier to a view and returns a new view.
- [protocol ViewModifier](./viewmodifier.md)
  A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [struct EmptyModifier](./emptymodifier.md)
  An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [protocol EnvironmentalModifier](./environmentalmodifier.md)
  A modifier that must resolve to a concrete modifier in an environment before use.
- [struct ManipulableModifier](./manipulablemodifier.md)
  A view modifier that lets hand gestures move, rotate, and scale a view.
- [struct ManipulableResponderModifier](./manipulablerespondermodifier.md)
  A view modifier that makes a view respond to manipulation hand gestures.
- [struct ManipulableTransformBindingModifier](./manipulabletransformbindingmodifier.md)
  A view modifier that applies a 3D affine transform to a view and lets hand gestures change it.
- [struct ManipulationGeometryModifier](./manipulationgeometrymodifier.md)
  A view modifier that tracks the geometry a manipulation gesture acts on.
- [struct ManipulationGestureModifier](./manipulationgesturemodifier.md)
  A view modifier that recognizes manipulation hand gestures and reports their state through a binding.
- [struct ManipulationUsingGestureStateModifier](./manipulationusinggesturestatemodifier.md)
  A view modifier that applies the manipulation state from a gesture on another view.
- [enum Manipulable](./manipulable.md)
  A namespace for various manipulable related types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/modifiedcontent)*