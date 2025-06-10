# UIDatePicker

**Framework**: UIKit  
**Kind**: class

A control for inputting date and time values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDatePicker
```

#### Overview

You can use a date picker to allow a user to enter either a point in time (calendar date, time value, or both) or a time interval (for example, for a timer). The date picker reports interactions to its associated target object.

To add a date picker to your interface:

- Set the date picker mode at creation time.
- Supply additional configuration options such as minimum and maximum dates if required.
- Connect an action method to the date picker.
- Set up Auto Layout rules to govern the position of the date picker in your interface.

You use a date picker only for handling the selection of times and dates. If you want to handle the selection of arbitrary items from a list, use a [`UIPickerView`](uipickerview.md) object.

##### Configure a Date Picker

The [`datePickerMode`](uidatepicker/datepickermode.md) property determines the configuration of a date picker. You can set the [`datePickerMode`](uidatepicker/datepickermode.md) value programmatically or in Interface Builder. For modes that include date or time values, you can also configure the locale, calendar, and time zone information. The date picker uses that information when formatting date and time values for the current user, and defaults to the device’s locale, calendar, and time zone. The [`date`](uidatepicker/date.md) property represents the currently selected date in the form of an [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) object, which is calendar and time zone agnostic.

To limit the range of dates that the user can select, assign values to the [`minimumDate`](uidatepicker/minimumdate.md) and [`maximumDate`](uidatepicker/maximumdate.md) properties. You can also use the [`minuteInterval`](uidatepicker/minuteinterval.md) property to allow only specific time increments.

Setting the [`datePickerMode`](uidatepicker/datepickermode.md) property to [`UIDatePicker.Mode.countDownTimer`](uidatepicker/mode/countdowntimer.md) allows the user to choose a duration in hours and minutes. When in this mode, the [`countDownDuration`](uidatepicker/countdownduration.md) property represents the displayed duration, measured in seconds as an [`TimeInterval`](https://developer.apple.com/documentation/Foundation/TimeInterval). Note that even though you set this property in seconds, the date picker can only show values in minutes.

The figure below shows a date picker configured with the [`datePickerMode`](uidatepicker/datepickermode.md) property set to [`UIDatePicker.Mode.countDownTimer`](uidatepicker/mode/countdowntimer.md) and the [`minuteInterval`](uidatepicker/minuteinterval.md) property set to `5`. The value of [`countDownDuration`](uidatepicker/countdownduration.md) is currently `4500`.

![A screenshot of a wheels-style date pickering showing the selected value of 1 hour and 15 minutes.](https://docs-assets.developer.apple.com/published/b2e540a05def72391939e2cef1050d68/media-2279158%402x.png)

> **Note**:  You can use a [`UIDatePicker`](uidatepicker.md) object for the selection of a time interval, but you must use an [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) object to implement the actual timer behavior. For more information, see [`Timer`](https://developer.apple.com/documentation/Foundation/Timer).

##### Respond to User Interaction

Date pickers use the target-action design pattern to notify your app when the user changes the selected date. To be notified when the date picker’s value changes, register your action method with the [`valueChanged`](uicontrol/event/valuechanged.md) event. At runtime the date picker calls your methods in response to the user selecting a date or time.

You connect a date picker to your action method using the [`addTarget(_:action:for:)`](uicontrol/addtarget(_:action:for:).md) method or by creating a connection in Interface Builder. The signature of an action method takes one of three forms, as shown in the following code. Choose the form that provides the information that you need to respond to the value change in the date picker.

##### Debug Date Pickers

When debugging issues with date pickers, watch for these common pitfalls:

-  Check the bounds of your [`minimumDate`](uidatepicker/minimumdate.md) and [`maximumDate`](uidatepicker/maximumdate.md) properties. If the maximum date is less than the minimum date, both properties are ignored, and the date picker allows the selection of any date value. The minimum and maximum dates are ignored in the countdown-timer mode ([`UIDatePicker.Mode.countDownTimer`](uidatepicker/mode/countdowntimer.md)).
-  Check that the [`minuteInterval`](uidatepicker/minuteinterval.md) value can be evenly divided into 60; otherwise, the default value is used (`1`).

##### Configure Date Picker Attributes in Interface Builder

The following table lists the core attributes that you configure for date pickers in Attributes Inspector within Interface Builder.

| Attribute | Description |
| --- | --- |
| Style | The date picker style. Determines the appearance of the date picker. Access this value at runtime with the [`datePickerStyle`](uidatepicker/datepickerstyle.md) property. |
| Mode | The date picker mode. Determines whether the date picker should display a time, a date, a time and date, or a countdown interval. Access this value at runtime with the [`datePickerMode`](uidatepicker/datepickermode.md) property. |
| Locale | The locale associated with the date picker. This property allows you to override the system default with a specific locale. You can access this attribute programmatically with the [`locale`](uidatepicker/locale.md) property. |
| Interval | The granularity of the minutes spinner, if it is shown in the current mode. The default value is 1, and the maximum value is 30. The value you choose must be a divisor of 60 (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30). Access this value at runtime with the [`minuteInterval`](uidatepicker/minuteinterval.md) property. |

The following table lists the attributes that control the display of date and time in a date picker.

| Attribute | Description |
| --- | --- |
| Date | The initial date that the date picker displays. Defaults to the current date, but you can set a custom value. This attribute is equivalent to setting the [`date`](uidatepicker/date.md) property programmatically. |
| Constraints | The range of selectable dates displayed by the date picker. To use a dynamic range, configure the [`minimumDate`](uidatepicker/minimumdate.md) and [`maximumDate`](uidatepicker/maximumdate.md) properties programmatically. The date picker ignores these options when the Mode attribute is set to Count Down Timer. |
| Timer | The initial value of the date picker when used in countdown timer mode. The value is measured in seconds, but the display is in minutes. |

For information about the date picker’s inherited Interface Builder attributes, see [`UIControl`](uicontrol.md) and [`UIView`](uiview.md).

##### Change the Appearance

You can change the appearance of [`UIDatePicker`](uidatepicker.md) by setting [`preferredDatePickerStyle`](uidatepicker/preferreddatepickerstyle.md). For a list of appearance styles, see [`UIDatePickerStyle`](uidatepickerstyle.md).

You should integrate date pickers in your layout using Auto Layout. Although date pickers can be resized, they should be used at their intrinsic content size.

##### Specify a Locale

Date pickers handle their own internationalization; the only thing you need to do is specify the appropriate locale. You can choose a specific locale for your date picker to appear in by setting the Locale ([`locale`](uidatepicker/locale.md)) field in Attributes Inspector. Setting the locale changes the language that the date picker uses for display, but also the format of the date and time (for example, certain locales present days before month names, or prefer a 24-hour clock over a 12-hour clock). The width of the date picker automatically accommodates for the length of the localization. To use the system language, leave this property set to default.

For more information, see [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).

##### Support Accessibility and Voiceover

Date pickers are accessible by default. Each time component in the date picker is its own accessibility element and has the Adjustable ([`adjustable`](uiaccessibilitytraits/adjustable.md)) trait.

The device reads the accessibility value, traits, and hint out loud for each date picker when the user enables VoiceOver. VoiceOver speaks this information when a user taps on a picker wheel. For example, when a user taps the hours column on the Add Alarm page (Clock > Alarm > Add), VoiceOver speaks the following:

```objc
"2 o'clock. Picker item. Adjustable. Swipe up or down with one finger to adjust the value."
```

For further information about making iOS controls accessible, see the [`Accessibility Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008785).

## Topics

### Managing the date and calendar
- [var calendar: Calendar!](uidatepicker/calendar.md)
  The calendar to use for the date picker.
- [var date: Date](uidatepicker/date.md)
  The date displayed by the date picker.
- [var locale: Locale?](uidatepicker/locale.md)
  The locale used by the date picker.
- [func setDate(Date, animated: Bool)](uidatepicker/setdate(_:animated:).md)
  Sets the date to display in the date picker, with an option to animate the setting.
- [var timeZone: TimeZone?](uidatepicker/timezone.md)
  The time zone reflected in the date displayed by the date picker.
### Configuring the date picker mode
- [var datePickerMode: UIDatePicker.Mode](uidatepicker/datepickermode.md)
  The mode of the date picker.
- [UIDatePicker.Mode](uidatepicker/mode.md)
  The mode displayed by the date picker.
### Configuring the date picker style
- [var datePickerStyle: UIDatePickerStyle](uidatepicker/datepickerstyle.md)
  The current style of the date picker.
- [var preferredDatePickerStyle: UIDatePickerStyle](uidatepicker/preferreddatepickerstyle.md)
  The preferred style of the date picker.
- [enum UIDatePickerStyle](uidatepickerstyle.md)
  Styles that determine the appearance of a date picker.
### Configuring temporal attributes
- [var maximumDate: Date?](uidatepicker/maximumdate.md)
  The maximum date that a date picker can show.
- [var minimumDate: Date?](uidatepicker/minimumdate.md)
  The minimum date that a date picker can show.
- [var minuteInterval: Int](uidatepicker/minuteinterval.md)
  The interval at which the date picker should display minutes.
- [var countDownDuration: TimeInterval](uidatepicker/countdownduration.md)
  The value displayed by the date picker when the mode property is set to show a countdown time.
- [var roundsToMinuteInterval: Bool](uidatepicker/roundstominuteinterval.md)
  A Boolean value that determines whether the date rounds to a specific minute interval.

## Relationships

### Inherits From
- [UIControl](uicontrol.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Responding to control-based events using target-action](responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class UIControl](uicontrol.md)
  The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions.
- [class UIButton](uibutton.md)
  A control that executes your custom code in response to user interactions.
- [class UIColorWell](uicolorwell.md)
  A control that displays a color picker.
- [class UIPageControl](uipagecontrol.md)
  A control that displays a horizontal series of dots, each of which corresponds to a page in the app’s document or other data-model entity.
- [class UISegmentedControl](uisegmentedcontrol.md)
  A horizontal control that consists of multiple segments, each segment functioning as a discrete button.
- [class UISlider](uislider.md)
  A control for selecting a single value from a continuous range of values.
- [class UIStepper](uistepper.md)
  A control for incrementing or decrementing a value.
- [class UISwitch](uiswitch.md)
  A control that offers a binary choice, such as on/off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker)*