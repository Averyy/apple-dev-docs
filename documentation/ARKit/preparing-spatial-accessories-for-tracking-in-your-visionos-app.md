# Preparing spatial accessories for tracking in your visionOS app

**Framework**: ARKit

Prepare a spatial accessory for tracking by training a reference accessory file and integrating it into your visionOS app.

#### Overview

In visionOS, you can use accessory tracking to make spatial accessories available in your app and to other apps. Spatial accessories are electronic devices that communicate with visionOS to track their physical location and orientation in a person’s environment.

Use accessory tracking to create interactions such as:

- Enhancing a video-game experience by tracking movement of the game controller as input for steering or aiming.
- Creating 3D models or sculptures by tracking a stylus and using its position as a drawing input.
- Practicing recreational activities, like tennis, to track and perfect your swing.

On Apple Vision Pro, visionOS tracks the 3D position and orientation of a handheld spatial accessory and its components. To add accessory tracking to your app, start with a 3D model of a physical spatial accessory. Use Reality Composer Pro to bring in a USDZ model of your device, add LEDs for visual tracking, and annotate the IMU pose.

Using your 3D model asset, train a machine learning model with the accessory tracking tool to generate a `.referenceaccessory` file. Use the *reference accessory file* to track the physical accessory in your app, or make it available to other apps by exporting it system-wide.

![Two views of a yellow and black handheld flashlight-style spatial accessory with LED markers on its top surface: one showing the front, and one showing the rear panel with a power button and additional controls.](https://docs-assets.developer.apple.com/published/12a733087958583a5d7a4dd887e0f1a0/spatial-accessory%402x.png)

#### Ensure Your Items Are Suitable for Accessory Tracking

Before you start building the accessory model, verify that your spatial accessory meets the hardware and protocol requirements for tracking.

Trackable spatial accessories need to:

- Follow the [`Accessory Design Guidelines`](https://developer.apple.comhttps://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf), paying close attention to the Spatial Accessories section. The guide covers terminology, components, and how people interact with spatial accessories.
- Send HID reports only in response to a direct action from the person using the spatial accessory.
- Configure an LED constellation, a layout formed on the spatial accessory consisting of LEDs, suitable for visual tracking.

#### Bring Your Spatial Accessory to Apple Vision Pro

Apple Vision Pro cameras track spatial accessories using both the *inertial measurement unit* (IMU) and an *LED constellation* pattern on the physical device. The LED constellation is the arrangement of LEDs on your spatial accessory that the cameras use to determine the accessory’s position and orientation. visionOS learns about the spatial accessory through a model-training process that uses a 3D model of the physical spatial accessory, annotated with its IMU pose and LED constellation.

For specifications on LED placement, constellation uniqueness, material requirements, and distance-dependent design parameters, see the [`Accessory Design Guidelines`](https://developer.apple.comhttps://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).

#### Obtain a 3d Model of Your Object

Provide an annotated 3D model of your spatial accessory in USDZ format that includes your LED constellation and IMU pose information. The accessory tracking tool uses this information to train a machine learning model and generate the reference accessory file.

If you don’t have these assets, start with a base USDZ file: a raw geometry file without LED or IMU data. To create one, use computer-aided design (CAD) software to model your spatial accessory’s geometry, apply physically-based rendering (PBR) materials, then export the asset as a USDZ file. Add the required LED and IMU annotations in Reality Composer Pro, as described in [`Add LEDs to your 3D model`](preparing-spatial-accessories-for-tracking-in-your-visionos-app#Add-LEDs-to-your-3D-model.md).

When creating your 3D model, ensure that:

- The scale is as precise as possible and matches its specified units. If the scale doesn’t match the real-world spatial accessory, the augmentation appears offset and may appear either in front of or behind the object.
- The 3D model only has one mesh before exporting to USDZ. If your 3D model contains a large number of individual part meshes, merge them into a single mesh, then export to USDZ.
- The base USDZ is color accurate and matches the appearance of your physical spatial accessory.

#### Convert Your Model to Usd Format

If your model is already in USDZ format, skip to [`Add LEDs to your 3D model`](preparing-spatial-accessories-for-tracking-in-your-visionos-app#Add-LEDs-to-your-3D-model.md). If your model is in `OBJ`, `glTF`, `GLB`, `PLY`, `ABC`, or `STL` format, convert it to USD first.

If you already have modeled reference elements for the spatial accessory body or LEDs in one of these formats, convert them to USD. Additionally, if you authored a USDA file, use these same steps to create a USDZ. Annotate and inspect the converted USDZ files to preserve the required information.

> **Note**: File conversion requires macOS 16 or later.

To convert a USDA file to USDZ, open it in the Preview app, choose File > Export, then set the format to USDZ.

To batch-convert other supported formats, use the USD command line tools:

- Use `usdcat <inputFile> -o <output.usdc>` to convert a non-USD file to USDC format.
- Use `usdzip <output.usdz> -a <model.usdc>` to package the USDC file along with any resources into a USDZ package.

#### Add Leds to Your 3d Model

For the LED constellation, add the LED points that match the pose on the physical device so that the system can accurately track each part. To set up the LED constellation:

1. Open Reality Composer Pro.
2. Create a new project, enter the project name, then click Create Project.
3. In the Project Browser, click the Import Asset button, then choose your USDZ spatial accessory body file.

![The Project Browser in Reality Composer Pro with the Import Asset button highlighted in the toolbar.](https://docs-assets.developer.apple.com/published/f12cc3cc6332b5f440192b5b11c08dcd/spatial-accessory-import-asset%402x.png)

1. Control-click the imported file and choose Add to Scene.

![The Reality Composer Pro context menu with Add to Scene highlighted, and the imported flashlight model shown in the preview.](https://docs-assets.developer.apple.com/published/5ba3e6b6dcba58758c4c94e96ab5214e/spatial-accessory-add-to-scene%402x.png)

Map each LED as a single USD primitive, a basic geometric shape (such as a sphere, cube, or cylinder) that other entities can be built from in the USD file format. To add an LED point, click the Add button (+) at the bottom of the Scene navigator on the left and choose Add Child Entity > Geometry > Sphere from the menu.

![Reality Composer Pro showing the Add Child Entity menu with a sphere being added to the spatial accessory model.](https://docs-assets.developer.apple.com/published/6e911b26a2da0b1b279ff787d9391029/spatial-accessory-add-led%402x.png)

Rename the added primitive using the naming scheme `ACCESSORY_LED_01`, `ACCESSORY_LED_02`, and so on, numbering each LED you add. To rename it, click the name of the entity in the hierarchy view, press Return, change the name to the proper scheme, then press Return again to save.

![Reality Composer Pro showing a sphere renamed to ACCESSORY_LED_00 with its Transform Component visible in the inspector.](https://docs-assets.developer.apple.com/published/cc25b969dce1f892d712c425d5f5a58d/spatial-accessory-rename-led%402x.png)

Adjust the size of the LED and use the Transform section to the right of the viewport to specify the position and orientation for the LED of the object:

1. Place the LED at the surface of the object so that it’s visible in the rendered image.
2. Set the position and orientation as precisely as possible. `xcrun createml accessorytracker` uses the location information during training and the orientation information to validate the constellation before training begins.
3. Size your LEDs according to the distance at which your spatial accessory is intended to operate.

> **Note**: For specifications on LED sizing, see the [`Accessory Design Guidelines`](https://developer.apple.comhttps://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).

![Reality Composer Pro showing the Transform Component with position, rotation, and scale values for an LED, and the Radius field for sizing.](https://docs-assets.developer.apple.com/published/3247ca488cc38922693824078dfb6bb9/spatial-accessory-transform-led%402x.png)

##### Define the Material of the Led

Also in the Transform section, define the material of the LED. Make sure that:

- The LED material is opaque and visible on the surface of the spatial accessory model.
- The surface of the spatial accessory model matches its appearance in the real world.
- The texture resolution is less than or equal to 4096 x 4096 pixels.
- The material of the controller body is nonreflective and nontransparent.

##### Confirm Your Led Constellation

As you add more LEDs to the model to create the constellation, make sure your model has:

- Four or more LEDs visible at each viewing angle of interest, so the constellation has a distinct layout across different viewing angles to avoid ambiguity of the orientation.
- A physical distance between LEDs of at least double the expected blob diameter to avoid overlapping.
- Submillimeter precision for each 3D-LED coordinate and normal to achieve high tracking quality.

> **Note**: Address these requirements when designing your physical spatial accessory. You can’t correct these specifications when adding the LEDs to the model if you didn’t design your device to meet them.

##### Add the Imu Transform to the Model

In addition to the LED constellation, add the IMU transform to your model. The IMU transform defines the location and orientation of the IMU within the spatial accessory, representing the rotation and translation of the IMU frame relative to the USD frame.

To add the IMU transform, create an empty child entity, rename it to `ACCESSORY_IMU`, then use the Transform section to set its position and orientation to match the IMU placement in your physical spatial accessory, using your CAD design and IMU datasheet as reference. You can set or change the IMU pose later using the `update-object` command.

![Reality Composer Pro showing the ACCESSORY_IMU empty entity added to the spatial accessory model with its Transform Component visible.](https://docs-assets.developer.apple.com/published/037d967587b3ba73af86b8bcf477227d/spatial-accessory-add-imu%402x.png)

LEDs allow you to mark each section of the spatial accessory so visionOS accurately tracks each part. Because the spatial accessory moves dynamically, place LEDs in strategic spots for the most accurate tracking.

> ❗ **Important**: After exporting your annotated USDZ from Reality Composer Pro, open the file in Preview to verify that all materials and textures exported correctly. If any materials appear transparent, re-export the file.

#### Train Your Assets with the Accessory Tracking Tool

Use `xcrun createml accessorytracker` to create, configure, and train reference accessory files unique to your chosen spatial accessories. Training runs locally on your Mac and can take a day or two depending on your hardware.

##### Create a Training Workspace

Start by creating a new workspace package and adding your spatial accessories. Each accessory requires a name, a source USDZ file, and a uniform type identifier (UTI):

```shell
% xcrun createml accessorytracker create my-project.package \
    --object name="Game Controller" source=controller.usdz uti=com.example.game-controller \
    --object name="Stylus" source=stylus.usdz uti=com.example.stylus
```

The tool validates your source files and runs pretraining diagnostics. Review any errors or warnings from the validation process before continuing.

> **Note**: The tool ignores any animations, virtual cameras, and lights within the asset during training, treating them as static.

##### Inspect Your Accessories

Use the `inspect` command to review your accessories’ settings, including IMU transforms and coordinate frames:

```shell
% xcrun createml accessorytracker inspect my-project.package
```

To inspect a specific accessory by its UTI, use the following command:

```shell
% xcrun createml accessorytracker inspect my-project.package com.example.game-controller
```

##### Update Accessory Attributes

To modify an accessory after creating the workspace, use the `update-object`, `rename-object`, or `add-frame` commands. As long as you don’t change the source USDZ file, you don’t need to retrain the accessory.

For example, to provide a lightweight render model for apps to use:

```shell
% xcrun createml accessorytracker update-object my-project.package com.example.game-controller \
    render-model=left-simplified-no-leds.usdz
```

To add a coordinate frame:

```shell
% xcrun createml accessorytracker add-frame my-project.package com.example.game-controller \
    name=grip transform=1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1
```

##### Launch Training

After configuring your accessories, run the `train` command:

```shell
% xcrun createml accessorytracker train my-project.package
```

Training can take a day or two depending on the configuration of your Mac. A more advanced processor and additional RAM significantly improve the training time.

> **Note**: Apple Vision Pro can track up to two reference spatial accessories simultaneously.

#### Export the Reference Accessory File

When training is complete, export your workspace to produce the reference accessory file:

```shell
% xcrun createml accessorytracker export my-project.package \
    --destination output.referenceaccessory
```

The reference accessory file contains the trained model packaged with your 3D model assets in the `.referenceaccessory` file format. Use the USDZ file within the reference accessory for visualizing the tracking quality by rendering it as an overlay on the real-world spatial accessory, and as a guide for adding immersive effects.

#### Distribute Your Reference Accessory File

Apps need access to your `.referenceaccessory` file to use your accessory. By default, manufacturers can ship an app that exports the file system-wide. However, this means that people need to install your app to use your accessory.

To avoid this dependency, Apple recommends also making the `.referenceaccessory` file available for developers to download. Apps that bundle the file work with your accessory the moment it connects, with no dependency on your app being installed. When your app is installed, its exported declaration still takes precedence.

#### Integrate the Reference Accessory File Into Your App

For accessory tracking to work at runtime:

- Turn on the spatial accessory and configure the device to work with visionOS.
- Connect the spatial accessory over Bluetooth.
- Ensure your app is immersive or in the foreground.

After generating the reference accessory file, set up accessory tracking in your app using ARKit. For game controller-specific uses, be sure to track button inputs.

For a complete walkthrough of building an app that uses your reference accessory file with ARKit, see [`Working with generic spatial accessories`](https://developer.apple.com/documentation/visionOS/working-with-generic-spatial-accessories). For game controller integration, see [`Discovering and tracking spatial game controllers and styli`](https://developer.apple.com/documentation/GameController/discovering-and-tracking-spatial-game-controllers-and-styli).

## See Also

- [Working with generic spatial accessories](../visionOS/working-with-generic-spatial-accessories.md)
  Use generic spatial accessories to track purpose-built devices in your visionOS app.
- [class AccessoryTrackingProvider](accessorytrackingprovider.md)
  Provides the real time position of accessories in the user’s environment.
- [struct Accessory](accessory.md)
  Represents an accessory to be tracked.
- [struct AccessoryAnchor](accessoryanchor.md)
  Represents a tracked accessory.
- [Tracking accessories in volumetric windows](tracking-accessories-in-volumetric-windows.md)
  Translate the position and velocity of tracked handheld accessories to throw virtual balls at a stack of cans.
- [Tracking a handheld accessory as a virtual sculpting tool](tracking-a-handheld-accessory-as-a-virtual-sculpting-tool.md)
  Use a tracked accessory with Apple Vision Pro to create a virtual sculpture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/preparing-spatial-accessories-for-tracking-in-your-visionos-app)*