# INParameter

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A parameter of an interaction object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INParameter
```

```objc
@interface INParameter : NSObject
```

## Mentions

- [Configuring the View Controller for Your Custom Interface](../SiriKit/configuring-the-view-controller-for-your-custom-interface.md)

#### Overview

Use a parameter object to identify a property of an [`INInteraction`](./ininteraction.md) object. To fetch the value of the property, use the [`parameterValue(for:)`](./ininteraction/parametervalue%28for%29.md) method of the [`INInteraction`](./ininteraction.md) object.

You use parameters when configuring a custom user interface for your Siri or Maps interactions. SiriKit passes parameter objects to you during the configuration of your interface. When configuring your interface, you can also create parameter objects to represent properties that you display in addition to the ones that SiriKit provides.

## Topics

### Creating a Parameter Object
- [convenience init(for: AnyClass, keyPath: String)](./inparameter/init%28for,keypath%29.md)
  Creates a new parameter object using the specified key path and class information.
- [convenience init?<Root, Value>(keyPath: KeyPath<Root, Value>)](./inparameter/init%28keypath%29.md)
  Creates a new parameter object using the specified key path and class information.
### Getting the Parameter Details
- [var parameterKeyPath: String](./inparameter/parameterkeypath.md)
  The key path to a property of an interaction object.
- [var parameterClass: AnyClass](./inparameter/parameterclass.md)
  The type of object represented by this parameter.
### Managing Indexed Values
- [func index(forSubKeyPath: String) -> Int](./inparameter/index%28forsubkeypath%29.md)
  The index into the array at the specified portion of the key path.
- [func setIndex(Int, forSubKeyPath: String)](./inparameter/setindex%28_,forsubkeypath%29.md)
  Specifies which item of an array or ordered set to use for the parameter.
### Comparing Parameters
- [func isEqual(to: INParameter) -> Bool](./inparameter/isequal%28to%29.md)
  Returns a Boolean value indicating whether the specified parameter object represents the same property as the current parameter object.
### Initializers
- [init?(coder: NSCoder)](./inparameter/init%28coder%29.md)
- [convenience init(forClass: AnyClass, keyPath: String)](./inparameter/init%28forclass,keypath%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Custom UI for Siri and Maps
- [Creating an Intents UI Extension](../SiriKit/creating-an-intents-ui-extension.md)
  Create an Intents UI app extension to customize the interfaces displayed by Siri and Maps.
- [protocol INUIHostedViewControlling](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling)
  Methods for presenting custom content in the Siri and Maps interfaces.
- [protocol INUIHostedViewSiriProviding](https://developer.apple.com/documentation/intentsui/inuihostedviewsiriproviding)
  Methods for hiding portions of the default interfaces that Siri provides.
- [protocol INIntentSetImageKeyPath](./inintentsetimagekeypath.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inparameter)*