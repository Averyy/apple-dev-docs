# Deprecated modifiers

**Framework**: SwiftUI

Review unsupported modifiers and their replacements.

#### Overview

Avoid using deprecated modifiers in your app. Select a modifier to see the replacement that you should use instead.

## Topics

### Accessibility modifiers
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(identifier:).md)
  Uses the specified string to identify the view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(selectionidentifier:).md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(hint:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(activationPoint:)](view/accessibility(activationpoint:).md)
  Specifies the point where activations occur in the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(inputlabels:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(addtraits:).md)
  Adds the given traits to the view.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(removetraits:).md)
  Removes the given traits from this view.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(sortpriority:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
### Appearance modifiers
- [func colorScheme(ColorScheme) -> some View](view/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func listRowPlatterColor(Color?) -> some View](view/listrowplattercolor(_:).md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func background<Background>(Background, alignment: Alignment) -> some View](view/background(_:alignment:).md)
  Layers the given view behind this view.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](view/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func foregroundColor(Color?) -> some View](view/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func complicationForeground() -> some View](view/complicationforeground.md)
  Promotes this view to the foreground in a complication.
### Text modifiers
- [func autocapitalization(UITextAutocapitalizationType) -> some View](view/autocapitalization(_:).md)
  Sets whether to apply auto-capitalization to this view.
- [func disableAutocorrection(Bool?) -> some View](view/disableautocorrection(_:).md)
  Sets whether to disable autocorrection for this view.
### Auxiliary view modifiers
- [func navigationBarTitle(_:)](view/navigationbartitle(_:).md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(_:displayMode:)](view/navigationbartitle(_:displaymode:).md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](view/navigationbaritems(leading:).md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](view/navigationbaritems(leading:trailing:).md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<T>(trailing: T) -> some View](view/navigationbaritems(trailing:).md)
  Configures the navigation bar items for this view.
- [func navigationBarHidden(Bool) -> some View](view/navigationbarhidden(_:).md)
  Hides the navigation bar for this view.
- [func statusBar(hidden: Bool) -> some View](view/statusbar(hidden:).md)
  Sets the visibility of the status bar.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](view/contextmenu(_:).md)
  Adds a context menu to the view.
### Style modifiers
- [func menuButtonStyle<S>(S) -> some View](view/menubuttonstyle(_:).md)
  Sets the style for menu buttons within this view.
- [func navigationViewStyle<S>(S) -> some View](view/navigationviewstyle(_:).md)
  Sets the style for navigation views within this view.
### Layout modifiers
- [func frame() -> some View](view/frame.md)
  Positions this view within an invisible frame.
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](view/edgesignoringsafearea(_:).md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.
- [func coordinateSpace<T>(name: T) -> some View](view/coordinatespace(name:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
### Graphics and rendering modifiers
- [func accentColor(Color?) -> some View](view/accentcolor(_:).md)
  Sets the accent color for this view and the views it contains.
- [func mask<Mask>(Mask) -> some View](view/mask(_:).md)
  Masks this view using the alpha channel of the given view.
- [func animation(Animation?) -> some View](view/animation(_:)-1hc0p.md)
  Applies the given animation to all animatable values within this view.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](view/cornerradius(_:antialiased:).md)
  Clips this view to its bounding frame, with the specified corner radius.
### Input and events modifiers
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](view/onchange(of:perform:).md)
  Adds an action to perform when the given value changes.
- [func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform: (CGPoint) -> Void) -> some View](view/ontapgesture(count:coordinatespace:perform:)-36x9h.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](view/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](view/onlongpressgesture(minimumduration:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) -> some View](view/onpastecommand(of:perform:)-4f78f.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) -> Payload?, perform: (Payload) -> Void) -> some View](view/onpastecommand(of:validator:perform:)-964k1.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
- [func onDrop(of: [String], delegate: any DropDelegate) -> some View](view/ondrop(of:delegate:)-2vr9o.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.
- [func onDrop(of:isTargeted:perform:)](view/ondrop(of:istargeted:perform:).md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View](view/focusable(_:onfocuschange:).md)
  Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus.
- [func onContinuousHover(coordinateSpace: CoordinateSpace, perform: (HoverPhase) -> Void) -> some View](view/oncontinuoushover(coordinatespace:perform:)-8gyrl.md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
### View presentation modifiers
- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](view/actionsheet(ispresented:content:).md)
  Presents an action sheet when a given condition is true.
- [func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View](view/actionsheet(item:content:).md)
  Presents an action sheet using the given item as a data source for the sheet’s content.
- [func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View](view/alert(ispresented:content:).md)
  Presents an alert to the user.
- [func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View](view/alert(item:content:).md)
  Presents an alert to the user.
### Search modifiers
- [func searchable(text:placement:prompt:suggestions:)](view/searchable(text:placement:prompt:suggestions:).md)
  Marks this view as searchable, which configures the display of a search field.
### Tab modifiers
- [func tabItem<V>(() -> V) -> some View](view/tabitem(_:).md)
  Sets the tab bar item associated with this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-deprecated)*