# Importing and organizing content in your project

**Framework**: Reality Composer Pro

Manage content in your Reality Composer Pro project with the Project Browser.

#### Overview

As you add content to your Reality Composer Pro document, the Project Browser displays the project’s structure and content, providing an interface with which to organize and view content details. By default, the Project Browser is the first editor displayed in the editor view. You can select the Project Browser tab to switch to it. Alternatively, you can select View > Project Browser in the menu bar.

![A screenshot of Reality Composer Pro’s Project Browser editor. The editor is divided into three views with a hierarchy on the left, a grid of icons in the middle, and an inspector on the right.](https://docs-assets.developer.apple.com/published/a52e999a1a09974cb1e423d01691d46b/ProjectBrowser.jpg)

The Project Browser contains three views:

-  for showing the current project structure and asset collections
-  for displaying the files in the currently selected folder
-  for displaying information about the currently selected file

##### View Your Projects Structure in Navigator View

All content in your Reality Composer Pro project is displayed in the navigator view. You can create new folders to organize content, and drag and drop files from the file view into folders in the navigator view. When you click on a folder in the navigator view, the file view updates to show the files within the folder.

##### Organize Your Projects Assets in File View

Reality Composer Pro displays files that are in the current folder in the file view. Typical interactions, such as cut, copy, paste, and delete are available. Double-clicking a file in the file view opens the selected file in its default editor.

> **Note**: When you select any `.usd` or `.usdz` files in the file view, the asset opens up a new scene tab with the asset loaded.

At the top of the file view is a toolbar that allows you to import additional content, create new folders, and create new scenes. On the right side of the toolbar is a slider to change the size of the icons, along with a dedicated search to quickly filter and find any content currently in the project.

##### Examine File Information in the Inspector View

Selecting a file in the file view updates the Project Browser’s inspector view, located to the right of the file view. The inspector displays information about the currently selected file and includes two tabs: hierarchy and information.

> **Note**: Reality Composer Pro represents all `.usd`, `.usdz`, and `.scene` files as 3D view thumbnails, along with a hierarchy view of contents and file information. Audio and image files display as thumbnails with related file information.

With the hierarchy tab selected in the inspector panel, you can drag and drop object into the navigator panel or the viewport to create a reference to them.

## See Also

- [Designing materials with Shader Graph](editor_shadergraph.md)
  Create realistic materials with Shader Graph’s node editor in Reality Composer Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/editor_projectbrowser)*