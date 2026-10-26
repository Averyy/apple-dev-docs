# configureView(for:of:interactiveBehavior:context:completion:)

**Framework**: IntentsUI  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func configureView(for parameters: Set<INParameter>, of interaction: INInteraction, interactiveBehavior: INUIInteractiveBehavior, context: INUIHostedViewContext, completion: @escaping (Bool, Set<INParameter>, CGSize) -> Void)
```

```swift
optional func configureView(for parameters: Set<INParameter>, of interaction: INInteraction, interactiveBehavior: INUIInteractiveBehavior, context: INUIHostedViewContext) async -> (Bool, Set<INParameter>, CGSize)
```

```objc
- (void) configureViewForParameters:(NSSet<INParameter *> *) parameters ofInteraction:(INInteraction *) interaction interactiveBehavior:(INUIInteractiveBehavior) interactiveBehavior context:(INUIHostedViewContext) context completion:(void (^)(BOOL success, NSSet<INParameter *> *configuredParameters, CGSize desiredSize)) completion;
```

## Mentions

- [Configuring the View Controller for Your Custom Interface](../../SiriKit/configuring-the-view-controller-for-your-custom-interface.md)

#### Discussion

Implement this method when you want to replace some or all of the default interface displayed by Siri or Maps as part of confirming or handling an intent. This method gives you granular control over the replacement of the content in the presented interface. If you implement this method, SiriKit calls this method instead of the [`configure(with:context:completion:)`](./configure%28with,context,completion%29.md) method.

Each interface presented by Siri or Maps contains information from the original intent object or from your response. Before constructing the interface, SiriKit builds a list of properties from those objects that it intends to display. For example, when displaying information about a booked ride, SiriKit might want to display the estimated pickup time, the pickup location, and the driver’s name and picture from your response object. It wraps each property in an [`INParameter`](https://developer.apple.com/documentation/intents/inparameter) object, which you use to retrieve the value of the property later.

SiriKit always calls this method on a unique instance of your view controller class. After asking you to configure the title view of the interface, SiriKit calls this method once with zero parameters. You can use that call to provide a custom view with any content you want. If there are still parameters to be displayed, SiriKit calls this method one or more additional times with a set of [`INParameter`](https://developer.apple.com/documentation/intents/inparameter) objects. Use each method call to configure the view controller’s view with the relevant parameter information. You can also configure the view with parameters not in the original set. For example, if SiriKit asks you to display only the pickup location, you might choose to display the pickup location, drop-off location, and pickup time together in the same view.

After using this method to configure the view controller, call the `completion` handler block and tell SiriKit which parameters your interface displays. (SiriKit does not ask you to configure view controllers for parameters that you already displayed.) If you specify [`false`](../../Swift/false.md) for the completion handler’s success parameter, SiriKit displays a default view for the corresponding parameters.

## Parameters

- `parameters`: The set of intent parameters that SiriKit intended to display. Sets contain one or more parameters, but may also include zero parameters. Each item in the set specifies a key path to a property of the response object in the `interaction` parameter. Use these key paths to identify which properties are being displayed by SiriKit.
- `interaction`: The interaction object containing the intent that was handled and your response. Use the information in this object to configure the content of your view controller’s view.
- `interactiveBehavior`: The behavior that SiriKit performs when the user taps on the view.
- `context`: The context in which your view controller is displayed. Use this parameter to determine whether your view controller is to be displayed in the Maps or Siri interface. You can customize your view controller accordingly for each interface.
- `completion`: The handler block to execute when you finish configuring your view controller. You must execute this handler at some point in your implementation of this method. This handler has no return value and takes the following parameters:

  - **success**: A Boolean value indicating whether you configured your view controller. Specify `true` if you configured your view controller and it is ready to display your custom interface. Specify `false` if you want SiriKit to display the default interface for the specified parameters.
  - **configuredParameters**: The set of parameters that your interface actually displays. SiriKit uses this information to determine what information you displayed and how it should proceed with constructing the user interface. For example, SiriKit avoids configuring additional views if your interface covers the parameters that those views would have displayed.
  - **desiredSize**: The size you want applied to the view controller’s view. Specify a value that is between the allowed minimum and maximum size, which you can get from the view controller’s associated [`NSExtensionContext`](../../Foundation/nsextensioncontext.md) object. Specify [`CGRectZero`](../../CoreGraphics/cgrectzero.md) to hide your view controller’s content altogether.

## See Also

### Configuring the View Controller
- [enum INUIInteractiveBehavior](../inuiinteractivebehavior.md)
  Constants indicating how users are able to interact with your interface.
- [func configure(with: INInteraction, context: INUIHostedViewContext, completion: (CGSize) -> Void)](./configure%28with,context,completion%29.md)
  Configures your view controller’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling/configureview(for:of:interactivebehavior:context:completion:))*