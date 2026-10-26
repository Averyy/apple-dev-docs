# Preparing plug-ins for use in Final Cut Pro

**Framework**: Professional-Video-Applications  
**Role**: Article

Add a plug-in to a Motion effect template to use in Final Cut Pro.

#### Overview

To make FxPlug plug-ins work in Final Cut Pro, you need to create a Final Cut Effect within Motion that rigs and/or publishes your FxPlug parameters. For more information, see [Rigging overview](https://support.apple.com/kb/PH16018) in Motion Help and [Final Cut Pro Templates Overview](https://support.apple.com/kb/PH16033).

> **Note**:  Final Cut Pro for iPad doesn’t support FxPlug 4 plug-ins.

Effects in Final Cut Pro include Generators, Transitions, and Filters. These Final Cut Pro effects are really just Motion documents, which can contain whatever you choose. This is useful because most users of Final Cut Pro want to solve specific tasks, rather than to apply particular effects with dozens of parameters. Advanced users who need more control will be able to either open your Final Cut Effect in Motion and edit it themselves, or create their own Final Cut Pro Effects within Motion for their specific task.

> **Note**:  In general, plug-in users don’t need control over every aspect of a plug-in to get the effect; effects that offer too many parameters to the user can be overwhelming.

To prepare your plug-in you use Motion to create a Final Cut Effect, Generator, Transition, or Title. To do that, you’ll need to create a Motion Effect, apply your filter or generator, and publish its parameters in a rig. A rig consolidates your plug-in’s parameters, which you can then publish in your effect. This makes it easier for Final Cut Pro users to apply the effects of your plug-in to their projects. (For information about creating rigs for your plug-in, see [Rigging overview](https://support.apple.com/kb/PH16018) in Motion Help).

##### Create a basic Final Cut Pro effect

The following steps outline the workflow for creating a basic Final Cut Pro Effect in Motion. For details about any step or about using Motion, see [Motion Help](https://help.apple.com/motion/mac/5.4.2/#/motn8d17a294).

1. Launch Motion and select the Final Cut Pro Effect template from the Project Browser. This creates a new Motion project with a placeholder layer called Effect Source.
2. Apply the Glow filter. You can do this by dragging the effect out of the filters library and onto the Effect Source placeholder. Alternatively, you can select the Effect Source placeholder layer, click Filters and choose Glow, and finally click Apply. Save your effect.
3. Open the filter’s Inspector. Select the newly applied Glow plug-in and open the Motion inspector to reveal the plug-in’s parameters.
4. Build and name a rig to connect the controls for the Radius parameter. Click the popup-menu indicator to the right of the Radius slider to see the options for the Radius parameter. Choose Add To Rig > Create New Rig > Add To New Slider. Motion creates a new Rig group in the layer list with the new layer (named Slider) selected. Change the name of the slider to Glowiness. Finally, choose Publish from the slider parameter’s option menu.
5. Connect the rig to the Opacity parameter. In the layer list, select the Glow filter to see its parameters in the Inspector. Parameters with a joystick icon indicate they’re controlled with a rig—notice that the Radius parameter shows this icon. Now, add another parameter to this rig. Click the pop-up menu indicator to the right of the Opacity slider and choose Add To Rig > Rig > Add To Glowiness.
6. Set the low end of parameters for the Glowiness effect. Select the rig named Glowiness in the layer list. In the inspector, you’ll see a slider that controls the parameter levels. On this slider, click the circle at the left end. Edit the levels for when Glowiness is set to zero. There are two parameters under this rig’s control: Opacity, and Radius. Set the Effect Source.Opacity and Effect Source.Radius sliders to 0. This sets the Opacity and Radius parameters to 0 when the rigged slider is set to 0.
7. Set the high end of parameters for the Glowiness effect. Now edit the right end of the rig. Begin again by clicking the circle at the right end of the Glowiness parameter. Next, set the Effect Source.Opacity and Effect Source.Radius sliders to their maximum values. You now have a rigged parameter. Drag the Glowiness parameter and verify that the underlying parameters change as well.

When you apply this plug-in in Final Cut Pro, users of the effect see a single slider (called Glowiness) which they can use to control both the Radius and Opacity parameters.

##### Publish the parameters for your plug-in

If you want to give your users direct access so they can control every aspect of a parameter in your plug-in, publish each parameter in Motion directly, without a rig. Unlike rigging a parameter, publishing a parameter gives users individual control over a single parameter.

To create the Threshold parameter for direct manipulation:

1. Show the filter’s parameters in the inspector. In the layer list, select the Glow effect and be sure the Inspector tab is visible.
2. Publish the Threshold parameter. In the inspector, click the Threshold parameter’s pop- up menu, and choose Publish.
3. Save the effect. When you attempt to save a Final Cut Pro Effect, Transition, Generator, or Title, you’re presented with some options. In addition to a name, you can assign the effect to a category, which is where it appears in the Final Cut Pro Effect browser. You can also add it to a theme. After you have a name and category, click the Publish button.

Your effect is immediately available in Final Cut Pro.

##### Set temporal effects and project loop markers

If your Motion Template doesn’t create a temporal effect (a timing effect such as retiming, temporal blur, or echo/feedback), set the Project Loop End marker in the template. If you don’t include such a marker, your effects will rerender after a blade, trim, or edit in Final Cut Pro. For more about Project Loop End markers, see [What are template markers?](https://support.apple.com/kb/PH16059)

##### Deprecate a Motion template

When you update an existing plug-in, you may also need to deprecate the older version of the Motion template. A deprecated template is considered obsolete and does not appear in the effects browser in Motion, but it will still be applied in projects that previously used it.

The second bit of the `<flags>` value in the Motion XML for a template indicates whether or not the template has been deprecated. A `0` value for the second bit indicates that the template has not been deprecated; a value of `1` indicates that it has been deprecated.

To deprecate a template, open the Motion XML document and take the current value of the `<flags>` element (a child of the `<template>` element) and perform a bitwise `OR` operation with the value `0x2`. For example, if the value of `<flags>` was previously `1`, it would now be `3`:

```other
<template>
    <flags>3</flags>
</template>
```

> **Note**:  If a project isn’t a Designed for 4K project, then the `<template>` element won’t exist in the XML document. To deprecate this type of project, manually add the `<template>` element and set `<flags>` to `2`.

## See Also

### Testing and deployment
- [Testing FxPlug plug-ins](./testing-fxplug-plug-ins.md)
  Test and debug FxPlug plug-ins using a variety of methods.
- [Notarizing your FxPlug plug-in](./notarizing-your-fxplug-plug-in.md)
  Give users confidence in your FxPlug plug-in by enabling notarization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/preparing-plug-ins-for-use-in-final-cut-pro)*