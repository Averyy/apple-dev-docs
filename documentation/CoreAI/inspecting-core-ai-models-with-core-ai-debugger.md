# Inspecting Core AI models with Core AI Debugger

**Framework**: Core AI

Verify model correctness by inspecting the operations and comparing tensor outputs.

#### Overview

Core AI Debugger is a standalone app for inspecting a Core AI model asset (`.aimodel`). The debugger follows a three-step workflow: visualize, execute, and validate. You visualize the model first to understand its structure, then execute the model to produce tensor outputs for each operation, and finally compare those outputs against a reference run to validate correctness. To download the app, see the [`Core AI Debugger`](https://developer.apple.comhttps://developer.apple.com/core-ai-debugger/) page.

> **Note**: If you have a PyTorch model that needs to be converted to an `.aimodel`, see the [`coreai-torch`](https://developer.apple.comhttps://apple.github.io/coreai-torch/main/getting-started/quickstart.html) documentation for guidance on how to convert your model.

#### Navigate the Workspace

The Core AI Debugger workspace includes a Navigator panel on the left, Structure and Source Viewers in the middle, and an Inspector to the right.

![The Core AI Debugger workspace showing a model loaded in single-session mode. The Navigator on the left lists model operations organized by PyTorch module in a tree hierarchy. The Structure Viewer in the center displays the model graph with the selected Pad operation highlighted and its connections visible. The Source Viewer below shows the corresponding Python source line highlighted. The Inspector on the right displays the selected operation’s description, parameters, attributes, and inputs.](/images/com.apple.coreai/inspecting-core-ai-models-with-core-ai-debugger-01@2x.png)

- Use the Navigator to explore, sort, and filter model operations.
- The Structure Viewer shows a graphical representation of the model as a series of connected operations, while the Source Viewer shows the model’s original Python source code, alongside a structured module hierarchy.
- Use the Inspector to see detailed metadata about the selected operation, including its description, inputs, and outputs.

The workspace stays synchronized around the selected operation, so you can move fluidly between structure, source, and execution details.

#### Visualize Model Structure

Opening an `.aimodel` file loads the model’s operations, structure, and source. Operations in the Navigator are organized by their PyTorch module. Selecting a module highlights the corresponding operations in the Structure Viewer, revealing their connectivity, data dependencies, and execution order. Clicking a specific operation highlights its Python source line in the Source Viewer. The Inspector shows additional details about the selected operation, including tensor formats of its inputs and outputs.

![The Core AI Debugger workspace with a module selected in the Navigator, highlighting its operations in the Structure Viewer. The Source Viewer below shows the corresponding Python source code in modeling_sam.py with the relevant line highlighted in blue. The Inspector on the right shows the selected operation’s tensor output as image thumbnails.](/images/com.apple.coreai/inspecting-core-ai-models-with-core-ai-debugger-02@2x.png)

The source-level features, including source line and PyTorch module mappings, require debug metadata embedded in the `.aimodel` at export time. Without this operation-level metadata, you can still view model operations in the Navigator, Structure Viewer, and the Inspector, but the Source Viewer is unavailable.

> **Note**: See the [`coreai-torch`](https://developer.apple.comhttps://apple.github.io/coreai-torch/main/api/debugging.html) documentation for details on how to export your model with debug metadata.

#### Execute on Specific Hardware

Configure a specialization scheme before executing your model. The scheme settings let you specify a hardware target, compute unit, and model inputs using predefined tensors (zeros, ones, or random) or values from a NumPy file.

![The scheme settings dialog in Core AI Debugger, showing Target set to Demo’s MacBook Pro, Function set to main, Compute Units set to Prefer GPU, and Graph Visualization set to Specialized. The Inputs section lists three model inputs (pixel_values, input_ids, and attention_mask) each configured as a NumPy Array. Cancel and Run buttons appear at the bottom.](/images/com.apple.coreai/inspecting-core-ai-models-with-core-ai-debugger-03@2x.png)

Clicking Run specializes the model for the selected target, optimizing it for that hardware’s capabilities. The Structure Viewer updates to show the specialized model exactly as it executes on the chosen device.

After running, click any operation in the Navigator or Structure Viewer to see its output tensor directly in the Inspector.

![The Core AI Debugger workspace after running the model on a MacBook Pro target. The Navigator on the left shows the specialized model’s operations. The Structure Viewer in the center displays the updated model graph. The Inspector on the right shows the selected Reshape operation’s description and its output tensor value alongside a grayscale thumbnail of the tensor.](/images/com.apple.coreai/inspecting-core-ai-models-with-core-ai-debugger-04@2x.png)

#### Validate Inference Correctness

A comparison session lets you identify where your model’s results diverge from a reference result. The debugger supports two comparison configurations:

- **Validate against a reference run.** Run your model in PyTorch and export the intermediate tensor values to an `aimodelintermediates` file using the [`coreai-torch`](https://developer.apple.comhttps://apple.github.io/coreai-torch/main/api/debugging.html) API. Open that file alongside your `.aimodel` to compare the results. For a detailed walkthrough, see [`Validating inference correctness against a reference run`](validating-inference-correctness-against-a-reference-run.md).

![The Core AI Debugger comparison session setup dialog, with Configuration A on the left configured with a MacBook Pro target, Prefer GPU compute units, and three NumPy Array inputs, and Configuration B on the right set to an Intermediates File target with a file path specified. The Compare button in the bottom right is highlighted in blue.](/images/com.apple.coreai/inspecting-core-ai-models-with-core-ai-debugger-05@2x.png)

- **Validate across configurations.** Configure two runs of the same `.aimodel` to compare execution across different hardware targets, compute units, or inputs.

Core AI Debugger compares two inference runs using *sync points*: operation pairs whose outputs are expected to match. When a comparison session starts, the debugger automatically identifies sync points and computes similarity metrics for each one so you can pinpoint where inference diverges.

## See Also

- [Validating inference correctness against a reference run](validating-inference-correctness-against-a-reference-run.md)
  Measure numerical divergence in a Core AI model against a reference run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inspecting-core-ai-models-with-core-ai-debugger)*