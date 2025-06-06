# CGEventField.keyboardEventKeycode

**Framework**: Core Graphics  
**Kind**: case

Key to access an integer field that contains the virtual keycode of the key-down or key-up event.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
case keyboardEventKeycode
```

## See Also

- [CGEventField.mouseEventNumber](cgeventfield/mouseeventnumber.md)
  Key to access an integer field that contains the mouse button event number. Matching mouse-down and mouse-up events will have the same event number.
- [CGEventField.mouseEventClickState](cgeventfield/mouseeventclickstate.md)
  Key to access an integer field that contains the mouse button click state. A click state of 1 represents a single click. A click state of 2 represents a double-click. A click state of 3 represents a triple-click.
- [CGEventField.mouseEventPressure](cgeventfield/mouseeventpressure.md)
  Key to access a double field that contains the mouse button pressure. The pressure value may range from 0 to 1, with 0 representing the mouse being up. This value is commonly set by tablet pens mimicking a mouse.
- [CGEventField.mouseEventButtonNumber](cgeventfield/mouseeventbuttonnumber.md)
  Key to access an integer field that contains the mouse button number. For information about the possible values, see [`CGMouseButton`](cgmousebutton.md).
- [CGEventField.mouseEventDeltaX](cgeventfield/mouseeventdeltax.md)
  Key to access an integer field that contains the horizontal mouse delta since the last mouse movement event.
- [CGEventField.mouseEventDeltaY](cgeventfield/mouseeventdeltay.md)
  Key to access an integer field that contains the vertical mouse delta since the last mouse movement event.
- [CGEventField.mouseEventInstantMouser](cgeventfield/mouseeventinstantmouser.md)
  Key to access an integer field. The value is non-zero if the event should be ignored by the Inkwell subsystem.
- [CGEventField.mouseEventSubtype](cgeventfield/mouseeventsubtype.md)
  Key to access an integer field that encodes the mouse event subtype as a `kCFNumberIntType`.
- [CGEventField.keyboardEventAutorepeat](cgeventfield/keyboardeventautorepeat.md)
  Key to access an integer field, non-zero when this is an autorepeat of a key-down, and zero otherwise.
- [CGEventField.keyboardEventKeyboardType](cgeventfield/keyboardeventkeyboardtype.md)
  Key to access an integer field that contains the keyboard type identifier.
- [CGEventField.scrollWheelEventDeltaAxis1](cgeventfield/scrollwheeleventdeltaaxis1.md)
  Key to access an integer field that contains scrolling data. This field typically contains the change in vertical position since the last scrolling event from a Mighty Mouse scroller or a single-wheel mouse scroller.
- [CGEventField.scrollWheelEventDeltaAxis2](cgeventfield/scrollwheeleventdeltaaxis2.md)
  Key to access an integer field that contains scrolling data. This field typically contains the change in horizontal position since the last scrolling event from a Mighty Mouse scroller.
- [CGEventField.scrollWheelEventDeltaAxis3](cgeventfield/scrollwheeleventdeltaaxis3.md)
  This field is not used.
- [CGEventField.scrollWheelEventFixedPtDeltaAxis1](cgeventfield/scrollwheeleventfixedptdeltaaxis1.md)
  Key to access a field that contains scrolling data. The scrolling data represents a line-based or pixel-based change in vertical position since the last scrolling event from a Mighty Mouse scroller or a single-wheel mouse scroller. The scrolling data uses a fixed-point 16.16 signed integer format. For example, if the field contains a value of 1.0, the integer 0x00010000 is returned by `CGEventGetIntegerValueField`. If this key is passed to `CGEventGetDoubleValueField`, the fixed-point value is converted to a double value.
- [CGEventField.scrollWheelEventFixedPtDeltaAxis2](cgeventfield/scrollwheeleventfixedptdeltaaxis2.md)
  Key to access a field that contains scrolling data. The scrolling data represents a line-based or pixel-based change in horizontal position since the last scrolling event from a Mighty Mouse scroller. The scrolling data uses a fixed-point 16.16 signed integer format. For example, if the field contains a value of 1.0, the integer 0x00010000 is returned by `CGEventGetIntegerValueField`. If this key is passed to `CGEventGetDoubleValueField`, the fixed-point value is converted to a double value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventfield/keyboardeventkeycode)*