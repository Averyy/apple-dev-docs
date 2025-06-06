# Arranging elements in a scene

**Framework**: RealityKit

Manipulate objects to complete your Reality Composer scene.

#### Overview

After you add assets to your Reality Composer scene, you can manipulate them in a number of ways to create your final scene. You assign names to objects and group them together to keep your project and code well organized. You can reposition, rotate, and scale assets relative to the scene’s anchor guides using the manipulator tool that appears whenever you select one or more objects. You can also use the Transform section of the Properties inspector to set precise transform values.

![Screenshot showing a Reality Composer window with an object selected so the manipulator controls are visible and the Properties inspector open.](https://docs-assets.developer.apple.com/published/5e97108f2a7efe221c0de4a93c3a3b8d/arranging-elements-in-a-scene-1%402x.png)

##### Move an Asset

To reposition an asset using the manipulator, tap or click the object to select it, then drag any of the three cone-shaped handles to move the object along the X (red), Y (green), or Z (blue) axis. You can also drag the object itself to move it up, down, left, or right relative to the current view.

To change the position of an asset using the Properties inspector, type the new X, Y, and Z value corresponding to the desired location using the Position text fields. You can specify a unit such as cm or m, or you can type just a number, which is interpreted in the currently displayed unit. For example, if the X position is currently displayed as 10 cm, and you type 100, Reality Composer interprets your input as 100 cm.

> **Note**: Reality Composer uses metric measurements by default. If you prefer to use imperial measurements such as feet and inches, you can make this change in Reality Composer’s preferences.

Reality Composer uses metric measurements by default. If you prefer to use imperial measurements such as feet and inches, you can make this change in Reality Composer’s preferences.

##### Rotate an Asset

To rotate the selected asset, drag the red, green, or blue manipulator ring corresponding to the axis you want to rotate in the direction you wish to rotate it. Reality Composer doesn’t display all three rotation rings at the same time. Instead, it displays one ring based on your current viewing angle. If the manipulator doesn’t show the ring for the axis you want to rotate, you can either rotate the scene view until the desired ring shows up, or you can tap or click the movement arrow of the same color as the axis you wish to rotate on, which causes the manipulator to show the desired rotation ring. You can also use the inspector to enter precise rotation values for each axis.

##### Scale an Asset

To scale the selected asset, drag the rotation ring away from the center of the object to scale up, or toward the center of the object to scale down. You can also change the scale using the Scale slider in the Properties inspector.

##### Toggle Snapping to Constrain Transforms

Toggle snapping by pressing the Snap button in the toolbar. The Snap option affects how the manipulator works, and it affects each of the transformation types differently. With position changes, Snap helps you align objects with the ground plane, or the center or edges of other objects based on their bounding boxes. When rotating an asset, Snap constrains rotation to 15-degree increments. When scaling an asset, the object will snap to 100 percent.

##### Change the Coordinate Space

By default, when you reposition an object using the manipulator, you move the object along the axes of the scene’s coordinate system (known as ). The X position manipulator, for example, always moves the object along the scene’s X-axis regardless of whether the object has been rotated.

Sometimes, you’ll want to move an object along its own rotated axes instead. Reality Composer allows you to toggle between the selected object’s coordinate system (known as ) and the scene’s coordinate system. Once you’ve switched to local space, the manipulator handles change position as you rotate the object, so that movement happens relative to the object’s current orientation.

To toggle between scene space and object space on a Mac, use the Space button on the toolbar or select the Space item from the Arrange menu.

![Image of the Space button showing different icons when in world space vs. local space](https://docs-assets.developer.apple.com/published/d5cf599de6c800acbfa538ad7e73ef1e/arranging-elements-in-a-scene-2.png)

To toggle between scene space and object space on an iOS device, tap the Settings button in the toolbar, then select either Transform World or Transform Local.

![Screenshot showing the portion of the Settings pane for Reality Composer for iOS, where you select between world and local transforms.](https://docs-assets.developer.apple.com/published/085643b4f82fb299f8ead0c9092a4366/arranging-elements-in-a-scene-3%402x.png)

##### Duplicate an Existing Asset

You can duplicate any asset in your scene. Duplicating an existing asset copies all of the parameter values that you’ve set in the Properties inspector except the asset’s position, which is offset from the original asset’s position to make the copy easier to find.

To duplicate an asset on the Mac, click an object in the scene view to select it, then click Duplicate in the Edit menu.

To duplicate an asset on an iOS device, select an object by tapping it in the scene view, then tap the selected object again to bring up a popover menu. From that menu, choose Duplicate.

##### Collect Assets Into Groups

You can combine multiple assets in a scene into a group. Grouped objects behave as a single combined object in Reality Composer’s scene view. Behaviors can target groups as well as individual objects inside a group. In code, a group is represented by an invisible [`Entity`](entity.md) with each of the grouped objects as its children.

> **Note**: If you’ve enabled physics in your scene, grouped objects still behave as separate, individual objects.

If you’ve enabled physics in your scene, grouped objects still behave as separate, individual objects.

To group items on the Mac, click the first object you want to include in the group to select it, then shift-click additional objects to add them to the selection. Once you select all the objects, choose Group from the Arrange menu. To ungroup items, select the group by clicking it in the scene view and choosing Ungroup from the Arrange menu.

To group items on an iOS device, touch and hold the first object you want to include in the group. While continuing to hold with the first finger, use another finger to tap additional objects to add them to the selection. You can deselect objects by tapping them a second time while continuing to hold your first finger down. When you’ve selected all the objects to groups, tap any of the selected objects to bring up an edit menu. From that menu, choose Group. To ungroup items, select the group by tapping it in the scene view, then tap again to bring up the edit menu, and choose Ungroup.

## See Also

- [Creating 3D Content with Reality Composer](creating-3d-content-with-reality-composer.md)
  Assemble assets into a dynamic 3D composition that you can add to a scene in your app, or share with AR Quick Look.
- [Loading Reality Composer files using generated code](loading-reality-composer-files-using-generated-code.md)
  Leverage automatically generated code to load scenes from Xcode.
- [Loading Reality Composer files manually without generated code](loading-reality-composer-files-manually-without-generated-code.md)
  Load Reality Composer files that aren’t part of your Xcode project.
- [Adding elements to a 3D scene](adding-elements-to-a-3d-scene.md)
  Add assets to your scene from Reality Composer’s library, or import custom assets.
- [Configuring elements in a scene](configuring-elements-in-a-scene.md)
  Define the appearance and behavior of objects in a scene.
- [Manipulating Reality Composer scenes from code](manipulating-reality-composer-scenes-from-code.md)
  Make programmatic changes to your scenes at runtime.
- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)
  Create procedurally generated shape primitives to your Reality Composer scene.
- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arranging-elements-in-a-scene)*