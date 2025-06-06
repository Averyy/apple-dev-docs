# Implementing a custom gesture recognizer

**Framework**: UIKit

Discover when and how to build your own gesture recognizers.

#### Overview

When the built-in UIKit gesture recognizers don’t provide the behavior you want, you can define custom gesture recognizers. UIKit defines highly configurable gesture recognizers to handle touch sequences for taps, long presses, pans, swipes, rotations, and pinches. For other touch sequences, or to handle gestures that involve button presses, you can define a custom gesture recognizer.

You might also use a custom gesture recognizer to simplify the event-handling code in your app. For example, the [`Leveraging touch input for drawing apps`](leveraging-touch-input-for-drawing-apps.md) sample uses a gesture recognizer to capture input and display it onscreen, as shown in the following image.

![A screenshot from an app which uses a custom gesture recognizer to allow a user to draw on the screen.](https://docs-assets.developer.apple.com/published/83675779848b8d1baece4a04cbbb6e88/media-2881148%402x.png)

To define a custom gesture recognizer, subclass [`UIGestureRecognizer`](uigesturerecognizer.md) (or one of its subclasses). At the top of your source file, import the `UIGestureRecognizerSubclass.h` header file (for Objective-C) or the `UIKit.UIGestureRecognizerSubclass` module (for Swift), as shown in the following code. This file defines the methods and properties that you must override to implement your custom gesture recognizer.

In your custom subclass, implement whatever methods you need to process events. For example, if your gesture consists of touch events, implement the [`touchesBegan(_:with:)`](uiresponder/touchesbegan(_:with:).md), [`touchesMoved(_:with:)`](uiresponder/touchesmoved(_:with:).md), [`touchesEnded(_:with:)`](uiresponder/touchesended(_:with:).md), and [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) methods. Use incoming events to update the [`state`](uigesturerecognizer/state-swift.property.md) property of your gesture recognizer. UIKit uses the gesture recognizer states to coordinate interactions with other objects in your interface.

## Topics

### Creating Custom Gesture Recognizers
- [About the Gesture Recognizer State Machine](about-the-gesture-recognizer-state-machine.md)
  Learn about the states and transitions of the state machine that underlies gesture recognizers.
- [Implementing a Discrete Gesture Recognizer](implementing-a-discrete-gesture-recognizer.md)
  If your gesture involves a specific pattern of events, consider implementing a discrete gesture recognizer for it.
- [Implementing a Continuous Gesture Recognizer](implementing-a-continuous-gesture-recognizer.md)
  For gestures that do not easily match a specific pattern, or when you want to use a gesture recognizer to gather touch input, create a continuous gesture recognizer.

## See Also

- [class UIGestureRecognizer](uigesturerecognizer.md)
  The base class for concrete gesture recognizers.
- [protocol UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md)
  A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md)
  Enrich your app’s user experience by supporting standard and custom gesture interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/implementing-a-custom-gesture-recognizer)*