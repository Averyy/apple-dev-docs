# Adding elements to a 3D scene

**Framework**: RealityKit

Add assets to your scene from Reality Composer’s library, or import custom assets.

#### Overview

To build a scene in , you import assets from usdz or Reality files, or select them from Reality Composer’s extensive library of configurable 3D objects you can customize by changing parameter values in the Properties inspector. Once the assets are in your scene, you can move, rotate, and scale them relative to the scene’s anchor guides. For more information about manipulating assets you’ve added to your scene, see [`Arranging elements in a scene`](arranging-elements-in-a-scene.md).

##### Add a Library Asset

To add an asset from ’s Object library, click or tap the plus button (+) in the toolbar to bring up the library popover, then drag the object you want into your scene view to place it.

![Screenshot showing a Reality Composer window with the Library palette open.](https://docs-assets.developer.apple.com/published/d5ccc1a8883f0efcf8556b5b41cc38c5/adding-elements-to-a-3d-scene-1.png)

Every library asset has a different set of parameters that you can change to alter its appearance. Although certain parameter sections, such as Transform and Physics, are available for all assets, most are available only when they make sense for the selected object. The clock asset, for example, lets you specify a time to display in the inspector, but other assets do not.

![Screenshot showing a clock asset with the Properties inspector visible.](https://docs-assets.developer.apple.com/published/4f74e9059cd6256697ff7016331630ee/adding-elements-to-a-3d-scene-2.png)

##### Import a Custom 3d Asset From a File

To import your own custom assets into a scene, use the Import button in the library popover, then navigate to a usdz or Reality file containing the asset you wish to import. On the Mac, you can also drag usdz or Reality files onto your Reality Composer project or select Import from the File menu.

The asset contained in the selected file is imported into your project and added to the current scene. Imported assets are available in Reality Composer’s library whenever you’re working with this project.

##### Create a Chart From a Data Source

Reality Composer’s library contains two chart assets: a pie chart and a bar chart. In addition to requiring you to provide parameter values for configuring their appearance, these two chart objects also require you to provide a data source in the form of a comma-separated values (CSV) file containing the data to be charted.

The CSV file requires two pieces of data for each item in the graph: a label and a numeric value. Your CSV file can represent the data you’re charting in columns or rows, and you can choose to include or exclude headers.

![An illustration showing a table of data and the chart that it would generate in Reality Composer.](https://docs-assets.developer.apple.com/published/0b7c69e4adfda77da8a090566689347c/adding-elements-to-a-3d-scene-3%402x.png)

If you tap or click a chart object in your scene, the Property inspector shows a button for importing a data source. Click or tap that button and select your CSV file. The chart then automatically updates to reflect the labels and values contained in the imported file.

## See Also

- [Loading Reality Composer files using generated code](loading-reality-composer-files-using-generated-code.md)
  Leverage automatically generated code to load scenes from Xcode.
- [Loading Reality Composer files manually without generated code](loading-reality-composer-files-manually-without-generated-code.md)
  Load Reality Composer files that aren’t part of your Xcode project.
- [Configuring elements in a scene](configuring-elements-in-a-scene.md)
  Define the appearance and behavior of objects in a scene.
- [Arranging elements in a scene](arranging-elements-in-a-scene.md)
  Manipulate objects to complete your Reality Composer scene.
- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)
  Create procedurally generated shape primitives to your Reality Composer scene.
- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/adding-elements-to-a-3d-scene)*